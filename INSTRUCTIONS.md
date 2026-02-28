# Instruções para Executar o Vault Indexer

## 1. Preparar o Ambiente

```bash
# Criar ambiente virtual (opcional)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

## 2. Configurar .env

Copie `.env.example` para `.env` e ajuste os caminhos:

```bash
cp .env.example .env
```

Edite o `.env` com:
- `VAULT_PATH`: Caminho absoluto para seu vault Obsidian
- `CHROMA_PERSIST_DIR`: Onde salvar o banco vetorial

## 3. Executar a Indexação

```bash
# Primeira vez (cria banco do zero)
python3 vault_indexer.py --clean

# Atualizar índice (adicionar novas notas)
python3 vault_indexer.py
```

## 4. Verificar Resultados

```bash
# O banco vetorial estará em ./chroma_db/
# Logs em indexing.log

# Verificar quantidade de documentos:
python3 -c "
import chromadb
client = chromadb.PersistentClient(path='./chroma_db')
col = client.get_or_create_collection('obsidian_notes')
print(f'Documentos: {col.count()}')
"
```

## Modelo de Embedding

- **Modelo:** `paraphrase-multilingual-MiniLM-L12-v2`
- **Dimensão:** 384
- **Multilíngue:** Suporta PT-BR nativamente
- **Nota:** Este modelo é ~4x menor que bge-m3 e muito mais rápido em CPU
