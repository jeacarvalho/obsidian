import os
import re
import hashlib
import logging
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional

import yaml
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv
from tqdm import tqdm
from sentence_transformers import SentenceTransformer


load_dotenv()

logging.basicConfig(
    filename="indexing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

VAULT_PATH = os.getenv("VAULT_PATH")
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "bge-m3")

EXCLUDE_DIRS = {
    ".obsidian",
    "templates",
    "attachments",
    "_processar",
    "_Processados",
    "_local",
    ".git",
}


def clean_frontmatter(text: str) -> Tuple[str, Dict]:
    """Remove frontmatter YAML e retorna metadados extraídos."""
    metadata = {}
    if text.startswith("---"):
        match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if match:
            try:
                metadata = yaml.safe_load(match.group(1)) or {}
            except yaml.YAMLError:
                pass
            text = text[match.end() :].strip()
    return text, metadata


def clean_obsidian_links(text: str) -> str:
    """Remove sintaxe [[ ]] mantendo texto do link."""
    text = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    return text


def clean_code_blocks(text: str) -> str:
    """Remove blocos de código ```."""
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"`[^`]+`", "", text)
    return text


def clean_note(text: str) -> str:
    """Aplica todas as limpezas no texto da nota."""
    text, _ = clean_frontmatter(text)
    text = clean_obsidian_links(text)
    text = clean_code_blocks(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def count_tokens(text: str) -> int:
    """Contagem aproximada de tokens (1 token ≈ 4 chars)."""
    return len(text) // 4


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100) -> List[str]:
    """Divide texto em chunks com overlap."""
    tokens = text.split()
    chunks = []
    start = 0

    while start < len(tokens):
        end = start + chunk_size * 4
        chunk = " ".join(tokens[start : end // 4])
        chunks.append(chunk)
        start += (chunk_size - overlap) * 4

    return chunks


EMBEDDING_MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
embedding_model = None


def get_embedding(text: str) -> Optional[List[float]]:
    """Gera embedding via sentence-transformers."""
    global embedding_model
    if embedding_model is None:
        embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    try:
        embedding = embedding_model.encode(text, convert_to_numpy=True)
        return embedding.tolist()
    except Exception as e:
        logging.error(f"Erro ao gerar embedding: {e}")
        return None


def scan_vault_notes(vault_path: str) -> List[Path]:
    """Escaneia o vault buscando arquivos .md."""
    notes = []
    vault = Path(vault_path)

    for md_file in vault.rglob("*.md"):
        if any(excluded in md_file.parts for excluded in EXCLUDE_DIRS):
            continue
        notes.append(md_file)

    logging.info(f"Encontradas {len(notes)} notas para processar")
    return notes


def process_note(note_path: Path) -> List[Dict]:
    """Processa uma nota e retorna chunks com metadados."""
    try:
        with open(note_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        logging.error(f"Erro ao ler {note_path}: {e}")
        return []

    cleaned = clean_note(content)
    title = note_path.stem

    tokens = count_tokens(cleaned)

    if tokens < 2000:
        chunks = [cleaned]
    else:
        chunks = chunk_text(cleaned, chunk_size=1500, overlap=150)

    results = []
    for i, chunk in enumerate(chunks):
        results.append(
            {
                "text": chunk,
                "file_path": str(note_path),
                "note_title": title,
                "chunk_id": i,
                "total_chunks": len(chunks),
            }
        )

    return results


def generate_doc_id(file_path: str, chunk_id: int) -> str:
    """Gera ID único para o documento."""
    raw = f"{file_path}_{chunk_id}"
    return hashlib.md5(raw.encode()).hexdigest()


def main(clean: bool = False):
    if not VAULT_PATH:
        raise ValueError("VAULT_PATH não definido no .env")

    vault = Path(VAULT_PATH)
    if not vault.exists():
        raise ValueError(f"Vault não encontrado: {VAULT_PATH}")

    logging.info(f"Usando modelo de embedding: {EMBEDDING_MODEL_NAME}")

    chroma_client = chromadb.PersistentClient(
        path=CHROMA_PERSIST_DIR, settings=Settings(anonymized_telemetry=False)
    )

    if clean:
        logging.info("Limpando banco vetorial existente...")
        try:
            chroma_client.delete_collection("obsidian_notes")
        except Exception:
            pass

    collection = chroma_client.get_or_create_collection(
        name="obsidian_notes", metadata={"model": EMBEDDING_MODEL_NAME}
    )

    notes = scan_vault_notes(VAULT_PATH)
    logging.info(f"Iniciando indexação de {len(notes)} notas")

    all_chunks = []

    for note_path in tqdm(notes, desc="Lendo notas"):
        chunks = process_note(note_path)
        all_chunks.extend(chunks)

    logging.info(f"Total de chunks gerados: {len(all_chunks)}")

    batch_size = 100
    for i in tqdm(range(0, len(all_chunks), batch_size), desc="Gerando embeddings"):
        batch = all_chunks[i : i + batch_size]

        ids = []
        embeddings = []
        documents = []
        metadatas = []

        for chunk in batch:
            doc_id = generate_doc_id(chunk["file_path"], chunk["chunk_id"])
            embedding = get_embedding(chunk["text"])

            if embedding:
                ids.append(doc_id)
                embeddings.append(embedding)
                documents.append(chunk["text"])
                metadatas.append(
                    {
                        "file_path": chunk["file_path"],
                        "note_title": chunk["note_title"],
                        "chunk_id": chunk["chunk_id"],
                        "total_chunks": chunk["total_chunks"],
                    }
                )

        if ids:
            collection.upsert(
                ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas
            )

    logging.info(f"Indexação concluída. Total de documentos: {collection.count()}")
    print(
        f"\n✓ Indexação concluída: {collection.count()} documentos salvos em {CHROMA_PERSIST_DIR}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--clean", action="store_true", help="Limpar banco vetorial antes de indexar"
    )
    args = parser.parse_args()

    main(clean=args.clean)
