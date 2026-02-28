# Vault Obsidian - Contexto do Agente

**Total de notas:** ~3.500

## Estrutura de Pastas Principais

| Pasta | Notas | Tema |
|-------|-------|------|
| 20 TEOLOGIA | 1.250 | Vida cristã, bíblia, ministério |
| 110 TRABALHO E GESTAO | 722 | Gestão, SERPRO |
| 50 VIDA SAUDAVEL | 465 | Saúde, low-carb |
| 90 FAMILIA | 188 | Vida familiar |
| 100 ARQUIVOS E REFERENCIAS | 168 | Bibliografia |
| 10 TI | 62 | Tecnologia |

## Pastas de Suporte
- `_admin` - Arquivos administrativos
- `templates/` - Templates (13 arquivos)
- `_processar/` - Notas para triagem (55)
- `raiz_nao_linkada/` - Notas órfãs

## Padrões do Vault
- Links wiki: `[[nota]]`
- Poucas notas usam frontmatter (~107 de ~3.500)
- Tags maioria vazias: `tags: []`
- Versionamento git ativo

## Skills Disponíveis
- **vault-context** - Contexto do vault
- **obsidian-markdown** - Formatação OFM
- **article-processing** - Processar artigos web
- **defuddle** - Extrair markdown de páginas
- **obsidian-bases** - Bases .base
- **json-canvas** - Arquivos .canvas
- **obsidian-cli** - CLI Obsidian

## Regras de Uso
1. No início de cada sessão, considerar o contexto do vault
2. Usar skills obsidian-markdown para formatação correta
3. Para artigos web, usar defuddle antes de salvar
4. Manter consistência com os padrões existentes

---

# Pipeline RAG: Livros → Notas do Vault

## Scripts Criados

### 1. `vault_indexer.py`
Indexa todas as notas do vault no ChromaDB para busca semântica.

**Uso:**
```bash
python3 vault_indexer.py --clean  # Primeira vez
python3 vault_indexer.py           # Atualizar índice
```

**Modelo de Embedding:** `paraphrase-multilingual-MiniLM-L12-v2` (384 dimensões)
- Multilíngue (PT-BR)
- ~4x menor e mais rápido que bge-m3 em CPU

### 2. `book_connector.py`
Conecta capítulos de livros às notas existentes do vault com validação via LLM.

**Uso:**
```bash
# Processar de capítulos extraídos
python3 book_connector.py "pasta/do/livro" --chapters

# Processar PDF direto
python3 book_connector.py "livro.pdf"

# Com tradução
python3 book_connector.py "livro.pdf" --no-translate
```

**Stack:**
- Extração: PyMuPDF (fitz) ou leitura direta de .md
- Tradução: Gemini 2.0 Flash
- Embeddings: sentence-transformers
- Vector Store: ChromaDB
- Validação: Ollama (llama3.2)

## Lições Aprendidas

### Problemas Encontrados e Soluções

1. **Embedding com Ollama CPU era muito lento**
   - Solução: Usar `sentence-transformers` local (~50x mais rápido)

2. **Modelos de embedding diferentes = dimensões incompatíveis**
   - Solução: Usar sempre `paraphrase-multilingual-MiniLM-L12-v2`

3. **Chunking gerava chunks vazios**
   - Solução: Corrigir lógica de split - usar tokens diretamente, não multiplicar por 4

4. **Trechos do livro eram retornados como matches**
   - Solução: Adicionar filtro `exclude_paths` na busca

5. **Validação Ollama muito lenta (timeout)**
   - Status: Não resolvido - precisa de modelo mais leve ou processamento paralelo

6. **Similaridade exibida incorretamente (0 ou 1)**
   - Solução: Usar `1 - distance` diretamente

## ToDo

- [ ] Otimizar validação Ollama (usar modelo mais leve: gemma2:2b)
- [ ] Implementar processamento incremental (salvar a cada chunk)
- [ ] Adicionar filtro por confiança mínima (atualmente 80%)
- [ ] Melhorar extração de chunks (remover notas relacionadas do final dos capítulos)
- [ ] Testar com outros livros
- [ ] Adicionar suporte a mais modelos de tradução

## Configuração (.env)

```bash
VAULT_PATH=/caminho/para/vault
CHROMA_PERSIST_DIR=./chroma_db
GEMINI_API_KEY=sua_chave
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2
EMBEDDING_MODEL=paraphrase-multilingual-MiniLM-L12-v2
```

---

## Workflow Antigo - Processamento de Livros PDF

Scripts em `_local/scripts/processar_livro.py`

### Funcionalidade
- Extrai texto de PDFs do Calibre
- Suporta chapters via arquivo externo (formato: pagina_inicio,pagina_fim)
- Ou detecta capítulos automaticamente (padrão "CHAPTER X")
- Traduz para português (via Langbly/Google/DeepL/AWS)
- Cria notas no vault com linking semântico para notas existentes

### Uso
```bash
# Processar livro com arquivo de capítulos (recomendado)
python3 _local/scripts/processar_livro.py "Nome do Livro" -c caminho/capitulos.txt

# Processar livro com detecção automática de capítulos
python3 _local/scripts/processar_livro.py "Nome do Livro"

# Processar com tradução
export LANGBLY_API_KEY="sua-chave"
python3 _local/scripts/processar_livro.py "Nome do Livro" -c caminho/capitulos.txt --traduzir

# Reconstruir índice de embeddings
python3 _local/scripts/processar_livro.py "Nome do Livro" --reindex
```

### Formato do arquivo de capítulos
```
# Exemplo: pagina_inicio,pagina_fim
7,25
26,50
51,75
76,100
...
```

### Estrutura de Notas Criadas
```
100 ARQUIVOS E REFERENCIAS/Livros/[Nome do Livro]/
├── Índice.md           # Visão geral + links para capítulos
├── 01 - Capítulo 1.md
├── 02 - Capítulo 2.md
└── ...
```

### Notas
- Embeddings armazenados em `_local/embeddings/` (fora do git)
- Módulos de tradução em `_local/scripts/translator/` (abstraídos para troca fácil)
- Busca semântica usa ChromaDB + sentence-transformers (paraphrase-multilingual-MiniLM-L12-v2)
