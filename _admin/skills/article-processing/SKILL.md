---
name: article-processing
description: Workflow para processar artigos web, extrair com defuddle, encontrar notas relacionadas no vault e criar nota com links. Use quando o usuário quiser salvar um artigo da web.
---

# Workflow: Processar Artigo Web

## Processo Completo

### 1. Extrair Artigo
```bash
defuddle parse <URL> --md
```

### 2. Analisar Conteúdo
- Identificar tema principal
- Extrair palavras-chave
- Identificar tecnologias/conceitos mencionados

### 3. Buscar Notas Relacionadas
```bash
grep -r "palavra-chave" --include="*.md"
```

Ou buscar por temas:
- Tecnologia → `10 TI/`
- Produtividade → `50 VIDA SAUDAVEL/`
- Trabalho → `110 TRABALHO E GESTAO/`

### 4. Criar Nota

Localização: `_processar/` (para triagem)

Frontmatter obrigatório:
```yaml
---
title: <título do artigo>
date: <AAAA-MM-DD>
tags: [<temas>]
author: <autor original>
source: <URL original>
type: artigo
status: para-revisar
---
```

Estrutura recomendada:
1. Resumo (2-3 linhas)
2. Seções principais do artigo
3. Notas relacionadas (usar wikilinks)

### 5. Criar Links

Para cada nota relacionada encontrada:
```markdown
- [[caminho/da/nota]] - motivo da conexão
```

---

## Exemplo de Resultado

Ver: `_processar/claude_code_fim_desenvolvimento.md`

---

## Dicas

- Buscar notas por temas, não apenas palavras exatas
- Priorizar notas com mais conexões
- Usar pasta `_processar` para artigos não revisados
- Após revisar, mover para pasta apropriada
