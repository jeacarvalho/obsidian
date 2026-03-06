---
name: article-processing
description: Workflow para processar artigos web, extrair com defuddle, encontrar notas relacionadas no vault e criar nota com links. Use quando o usuário quiser salvar um artigo da web.
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:55.587383+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: interacao_com_vault_obsidian
    weight: 10
    confidence: 0.98
  - name: gerenciamento_de_notas_obsidian
    weight: 9
    confidence: 0.97
  - name: criacao_de_notas_obsidian
    weight: 8
    confidence: 0.96
  - name: busca_em_vault_obsidian
    weight: 8
    confidence: 0.95
  - name: gerenciamento_de_tarefas_obsidian
    weight: 7
    confidence: 0.94
  - name: desenvolvimento_de_plugins_obsidian
    weight: 9
    confidence: 0.93
  - name: desenvolvimento_de_temas_obsidian
    weight: 8
    confidence: 0.92
  - name: execucao_de_javascript_em_obsidian
    weight: 7
    confidence: 0.91
  - name: depuracao_de_plugins_obsidian
    weight: 8
    confidence: 0.9
  - name: automacao_de_comandos_obsidian
    weight: 10
    confidence: 0.99
  cdu_primary: '004.4'
  cdu_secondary:
  - '004.77'
  - '004.8'
  - '004.9'
  cdu_description: Sistemas de computadores; Organização de computadores; Programação; Desenvolvimento de software; Aplicações de software; Ferramentas de linha de comando; Automação; Gerenciamento de notas digitais; Plugins e extensões.
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
