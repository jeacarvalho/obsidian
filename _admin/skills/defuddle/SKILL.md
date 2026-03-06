---
name: defuddle
description: Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch when the user provides a URL to read or analyze, for online documentation, articles, blog posts, or any standard web page.
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:55.722014+00:00'
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

# Defuddle

Use Defuddle CLI to extract clean readable content from web pages. Prefer over WebFetch for standard web pages — it removes navigation, ads, and clutter, reducing token usage.

If not installed: `npm install -g defuddle-cli`

## Usage

Always use `--md` for markdown output:

```bash
defuddle parse <url> --md
```

Save to file:

```bash
defuddle parse <url> --md -o content.md
```

Extract specific metadata:

```bash
defuddle parse <url> -p title
defuddle parse <url> -p description
defuddle parse <url> -p domain
```

## Output formats

| Flag | Format |
|------|--------|
| `--md` | Markdown (default choice) |
| `--json` | JSON with both HTML and markdown |
| (none) | HTML |
| `-p <name>` | Specific metadata property |
