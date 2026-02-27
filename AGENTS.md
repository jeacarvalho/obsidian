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

## Workflow - Processamento de Livros PDF

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
