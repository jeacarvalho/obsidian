import os
import re
import json
import logging
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

import fitz
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import google.genai as genai


load_dotenv()

logging.basicConfig(
    filename="book_connector.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

VAULT_PATH = os.getenv("VAULT_PATH")
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
PDFS_PATH = os.getenv("PDFS_PATH", "./pdfs")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "./output")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
TOP_K = 5
MIN_CONFIDENCE = 80  # Mínimo de confiança para aceitar match


@dataclass
class Chunk:
    text: str
    page_start: int
    page_end: int
    chunk_id: int


@dataclass
class Match:
    chunk: Chunk
    note_path: str
    note_title: str
    note_content: str
    similarity: float
    approved: bool
    confidence: int
    reason: str


def chunk_text(
    text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP
) -> List[str]:
    tokens = text.split()
    chunks = []
    start = 0

    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        if not chunk_tokens:
            break
        chunks.append(" ".join(chunk_tokens))
        start += chunk_size - overlap
        if start >= len(tokens):
            break

    return [c for c in chunks if c.strip()]


def extract_text_from_pdf(pdf_path: str) -> Tuple[str, List[int]]:
    doc = fitz.open(pdf_path)
    full_text = ""
    page_counts = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        full_text += text + "\n\n"
        page_counts.append(page_num + 1)

    doc.close()
    return full_text, page_counts


def extract_text_from_chapters(
    book_folder: str,
) -> Tuple[str, Dict[int, Tuple[int, int]]]:
    """Extrai texto de capítulos já processados no vault."""
    book_path = Path(book_folder)
    chapters = {}

    for chapter_file in sorted(book_path.glob("*.md")):
        if chapter_file.name == "Índice.md":
            continue

        match = re.match(r"(\d+)\s*-\s*Capítulo\s*(\d+)", chapter_file.stem)
        if not match:
            continue

        chapter_num = int(match.group(1))

        try:
            with open(chapter_file, "r", encoding="utf-8") as f:
                content = f.read()

            if content.startswith("---"):
                match_yaml = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
                if match_yaml:
                    content = content[match_yaml.end() :]

            sections = re.split(r"(?=^##\s+\d+)", content, flags=re.MULTILINE)
            text = "\n\n".join(sections)
            chapters[chapter_num] = text
            logging.info(f"Capítulo {chapter_num}: {len(text)} caracteres")

        except Exception as e:
            logging.error(f"Erro ao ler {chapter_file}: {e}")

    full_text = "\n\n=== CHAPTER {} ===\n\n".format(" || ").join(
        [f"CAPÍTULO {k}" + v for k, v in sorted(chapters.items())]
    )

    return full_text, {}


def translate_with_gemini(text: str, target_lang: str = "pt") -> str:
    if not GEMINI_API_KEY:
        logging.warning("GEMINI_API_KEY não definida, retornando texto original")
        return text

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        prompt = f"Traduza o seguinte texto para {target_lang}. Mantenha a formatação original:\n\n{text}"
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        return response.text
    except Exception as e:
        logging.error(f"Erro na tradução: {e}")
        return text


def is_portuguese(text: str) -> bool:
    pt_indicators = [
        "é",
        "ao",
        "dos",
        "das",
        "para",
        "com",
        "não",
        "uma",
        "como",
        "são",
    ]
    text_lower = text.lower()
    return sum(1 for word in pt_indicators if word in text_lower) >= 2


def get_embedding(text: str, model: SentenceTransformer) -> List[float]:
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding.tolist()


def search_similar_notes(
    query_embedding: List[float],
    collection,
    top_k: int = TOP_K,
    exclude_paths: List[str] = None,
) -> List[Dict]:
    if exclude_paths is None:
        exclude_paths = []

    # Get more results to filter out excluded ones
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k * 3)

    matches = []
    for i in range(len(results["ids"][0])):
        metadata = results["metadatas"][0][i]
        file_path = metadata.get("file_path", "")

        # Skip if path matches exclusion patterns
        skip = False
        for exclude in exclude_paths:
            if exclude.lower() in file_path.lower():
                skip = True
                break

        if not skip:
            matches.append(
                {
                    "id": results["ids"][0][i],
                    "document": results["documents"][0][i],
                    "metadata": metadata,
                    "distance": results["distances"][0][i]
                    if "distances" in results
                    else 0,
                }
            )

        if len(matches) >= top_k:
            break

    return matches


def read_note_content(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if content.startswith("---"):
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
            if match:
                content = content[match.end() :]

        return content.strip()
    except Exception as e:
        logging.error(f"Erro ao ler nota {file_path}: {e}")
        return ""


def validate_with_ollama(chunk_text: str, note_text: str) -> Optional[Dict]:
    import requests

    system_prompt = """Você é um curador de conhecimento MUITO RIGOROSO. 
Sua tarefa é validar conexões semânticas entre trechos de livros e notas pessoais.
Analise com CRÍTICA, não aceite conexões fracas ou apenas coincidência lexical.
Responda APENAS com JSON válido."""

    user_prompt = f"""Analise a relação semântica entre o trecho do livro e a nota do vault.

Trecho do Livro:
{chunk_text[:2000]}

Nota do Vault:
{note_text[:2000]}

Para APROVAR (approved: true), AMBAS as condições devem ser verdadeiras:
1. O TEMA CENTRAL deve ser o MESMO ou MUITO RELACIONADO (não apenas palavras similares)
2. Os CONCEITOS devem se COMPLEMENTAR ou APROFUNDAR mutuamente

Rejeite se:
- É apenas coincidência lexical (mesma palavra em contextos diferentes)
- Os temas são vagamente relacionados mas não conectados
- A nota é sobre algo genérico que pode aparecer em qualquer contexto

Responda APENAS JSON (sem markdown, sem texto adicional):
{{"approved": boolean, "confidence": 0-100, "reason": "explicação curta"}}"""

    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/chat",
            json={
                "model": OLLAMA_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "format": "json",
                "stream": False,
            },
            timeout=60,
        )

        if response.status_code == 200:
            result = response.json()
            content = result.get("message", {}).get("content", "{}")

            try:
                return json.loads(content)
            except json.JSONDecodeError:
                logging.error(f"JSON inválido: {content}")
                return {"approved": False, "confidence": 0, "reason": "Erro parsing"}
        else:
            logging.error(f"Ollama erro: {response.status_code}")
            return None

    except Exception as e:
        logging.error(f"Erro na validação Ollama: {e}")
        return None


def create_output_file(book_name: str, matches: List[Match], output_path: str):
    os.makedirs(output_path, exist_ok=True)

    output_file = os.path.join(output_path, f"{book_name}_Conexoes.md")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"validation_engine: ollama\n")
        f.write(f"validation_model: {OLLAMA_MODEL}\n")
        f.write(f"embedding_model: {EMBEDDING_MODEL}\n")
        f.write(f"status: approved\n")
        f.write(f"total_connections: {len(matches)}\n")
        f.write("---\n\n")

        f.write(f"# Conexões Validadas: {book_name}\n\n")

        for i, match in enumerate(matches, 1):
            f.write(f"## {i}. {match.note_title}\n\n")
            f.write(
                f"**Origem:** Página {match.chunk.page_start}-{match.chunk.page_end}\n\n"
            )
            f.write(f"**Similaridade:** {match.similarity:.3f}\n\n")
            f.write(f"**Confiança:** {match.confidence}%\n\n")
            f.write(f"**Motivo:** {match.reason}\n\n")
            f.write(f"**Trecho do Livro:**\n> {match.chunk.text[:300]}...\n\n")
            f.write(f"**Nota:** [[{match.note_title}]]\n\n")
            f.write("---\n\n")

    logging.info(f"Output salvo em: {output_file}")
    return output_file


def process_book(
    pdf_path: str,
    embedding_model: SentenceTransformer,
    collection,
    translate: bool = True,
) -> List[Match]:
    book_name = Path(pdf_path).stem
    logging.info(f"Processando: {book_name}")

    raw_text, page_counts = extract_text_from_pdf(pdf_path)
    logging.info(f"Texto extraído: {len(raw_text)} caracteres")

    if translate and not is_portuguese(raw_text):
        logging.info("Traduzindo para português...")
        raw_text = translate_with_gemini(raw_text)

    chunks_raw = chunk_text(raw_text)
    logging.info(f"Chunks gerados: {len(chunks_raw)}")

    all_matches = []

    for chunk_id, chunk_text_val in enumerate(
        tqdm(chunks_raw, desc=f"Processando {book_name}")
    ):
        chunk = Chunk(
            text=chunk_text_val,
            page_start=(chunk_id * (CHUNK_SIZE - CHUNK_OVERLAP)) // 4 + 1,
            page_end=((chunk_id + 1) * (CHUNK_SIZE - CHUNK_OVERLAP)) // 4 + 1,
            chunk_id=chunk_id,
        )

        query_embedding = get_embedding(chunk_text_val, embedding_model)
        similar_notes = search_similar_notes(query_embedding, collection)

        for note in similar_notes:
            note_path = note["metadata"]["file_path"]
            note_title = note["metadata"]["note_title"]
            distance = note.get("distance", 0)
            similarity = 1 - distance  # Distance is already the right metric

            if os.path.exists(note_path):
                note_content = read_note_content(note_path)
            else:
                note_content = note["document"]

            validation = validate_with_ollama(chunk_text_val, note_content)

            if (
                validation
                and validation.get("approved")
                and validation.get("confidence", 0) >= MIN_CONFIDENCE
            ):
                match = Match(
                    chunk=chunk,
                    note_path=note_path,
                    note_title=note_title,
                    note_content=note_content,
                    similarity=similarity,
                    approved=True,
                    confidence=validation.get("confidence", 0),
                    reason=validation.get("reason", ""),
                )
                all_matches.append(match)
                logging.info(
                    f"Match aprovado: {note_title} (confiança: {validation.get('confidence')})"
                )

    return all_matches


def process_from_chapters(
    book_folder: str,
    embedding_model: SentenceTransformer,
    collection,
) -> List[Match]:
    book_name = Path(book_folder).name
    logging.info(f"Processando capítulos de: {book_name}")

    raw_text, _ = extract_text_from_chapters(book_folder)
    logging.info(f"Texto extraído: {len(raw_text)} caracteres")

    chunks_raw = chunk_text(raw_text)
    logging.info(f"Chunks gerados: {len(chunks_raw)}")

    all_matches = []

    for chunk_id, chunk_text_val in enumerate(
        tqdm(chunks_raw, desc=f"Processando {book_name}")
    ):
        chapter_match = re.search(r"CAPÍTULO\s+(\d+)", chunk_text_val[:100])
        chapter_info = f"Capítulo {chapter_match.group(1)}" if chapter_match else "?"

        chunk = Chunk(
            text=chunk_text_val,
            page_start=chunk_id + 1,
            page_end=chunk_id + 1,
            chunk_id=chunk_id,
        )

        query_embedding = get_embedding(chunk_text_val, embedding_model)
        similar_notes = search_similar_notes(
            query_embedding,
            collection,
            exclude_paths=["100 ARQUIVOS E REFERENCIAS/Livros", "Idols of Nations"],
        )

        for note in similar_notes:
            note_path = note["metadata"]["file_path"]
            note_title = note["metadata"]["note_title"]
            distance = note.get("distance", 0)
            similarity = 1 - distance  # Distance is already the right metric

            if os.path.exists(note_path):
                note_content = read_note_content(note_path)
            else:
                note_content = note["document"]

            validation = validate_with_ollama(chunk_text_val, note_content)

            if (
                validation
                and validation.get("approved")
                and validation.get("confidence", 0) >= MIN_CONFIDENCE
            ):
                match = Match(
                    chunk=chunk,
                    note_path=note_path,
                    note_title=note_title,
                    note_content=note_content,
                    similarity=similarity,
                    approved=True,
                    confidence=validation.get("confidence", 0),
                    reason=validation.get("reason", ""),
                )
                all_matches.append(match)
                logging.info(
                    f"Match aprovado: {note_title} ({chapter_info}) - confiança: {validation.get('confidence')}"
                )

    return all_matches


def main(
    pdf_path: str = None,
    translate: bool = True,
    clean: bool = False,
    chapters_folder: str = None,
):
    if not VAULT_PATH:
        raise ValueError("VAULT_PATH não definido no .env")

    logging.info(f"Carregando modelo de embedding: {EMBEDDING_MODEL}")
    embedding_model = SentenceTransformer(EMBEDDING_MODEL)

    chroma_client = chromadb.PersistentClient(
        path=CHROMA_PERSIST_DIR, settings=Settings(anonymized_telemetry=False)
    )

    try:
        collection = chroma_client.get_collection("obsidian_notes")
    except Exception as e:
        raise ValueError(f"Coleção 'obsidian_notes' não encontrada: {e}")

    logging.info(f"Coleção carregada: {collection.count()} documentos")

    if chapters_folder:
        book_path = Path(chapters_folder)
        if not book_path.exists():
            raise ValueError(f"Pasta de capítulos não encontrada: {chapters_folder}")
        book_name = book_path.name
        output_file = os.path.join(OUTPUT_PATH, f"{book_name}_Conexoes.md")
        matches = process_from_chapters(chapters_folder, embedding_model, collection)
    else:
        if not os.path.exists(PDFS_PATH):
            raise ValueError(f"Pasta de PDFs não encontrada: {PDFS_PATH}")
        pdf_full_path = (
            os.path.join(PDFS_PATH, pdf_path)
            if not os.path.isabs(pdf_path)
            else pdf_path
        )
        if not os.path.exists(pdf_full_path):
            raise ValueError(f"PDF não encontrado: {pdf_full_path}")
        book_name = Path(pdf_path).stem
        output_file = os.path.join(OUTPUT_PATH, f"{book_name}_Conexoes.md")
        matches = process_book(pdf_full_path, embedding_model, collection, translate)

    if matches:
        output_path = create_output_file(book_name, matches, OUTPUT_PATH)
        print(f"\n✓ Processamento concluído!")
        print(f"  Conexões validadas: {len(matches)}")
        print(f"  Output: {output_path}")
    else:
        print("\n✓ Processamento concluído!")
        print("  Nenhuma conexão validada encontrada.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Conecta livros (PDF ou capítulos) a notas do Obsidian"
    )
    parser.add_argument(
        "input", nargs="?", help="Nome do arquivo PDF ou pasta de capítulos"
    )
    parser.add_argument(
        "--chapters",
        action="store_true",
        help="Usar capítulos extraídos do vault em vez de PDF",
    )
    parser.add_argument(
        "--no-translate", action="store_true", help="Desativar tradução"
    )
    parser.add_argument(
        "--clean", action="store_true", help="Sobrescrever output existente"
    )
    args = parser.parse_args()

    if args.chapters:
        chapters_path = args.input or "100 ARQUIVOS E REFERENCIAS/Livros"
        main(chapters_folder=chapters_path, clean=args.clean)
    else:
        if not args.input:
            print("Erro: Informe o nome do PDF ou use --chapters")
            exit(1)
        main(args.input, translate=not args.no_translate, clean=args.clean)
