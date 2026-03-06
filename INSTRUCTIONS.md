---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:41.425667+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: execucao_vault_indexer
    weight: 10
    confidence: 0.98
  - name: preparacao_ambiente_virtual
    weight: 8
    confidence: 0.95
  - name: instalacao_dependencias_python
    weight: 7
    confidence: 0.92
  - name: configuracao_arquivo_env
    weight: 9
    confidence: 0.96
  - name: definicao_caminho_vault_obsidian
    weight: 8
    confidence: 0.94
  - name: configuracao_diretorio_banco_vetorial
    weight: 8
    confidence: 0.94
  - name: execucao_script_vault_indexer
    weight: 9
    confidence: 0.97
  - name: limpeza_e_reconstrucao_indice
    weight: 7
    confidence: 0.9
  - name: atualizacao_indice_existente
    weight: 7
    confidence: 0.9
  - name: verificacao_quantidade_documentos_chromadb
    weight: 6
    confidence: 0.88
  cdu_primary: '004.4'
  cdu_secondary:
  - '004.7'
  - '004.8'
  cdu_description: Processamento de dados; Sistemas de computadores; Gerenciamento de dados
---
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
