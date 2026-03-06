---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:55.168994+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: gerenciamento_notas_obsidian
    weight: 10
    confidence: 0.98
  - name: plugins_obsidian
    weight: 9
    confidence: 0.97
  - name: markdown_obsidian
    weight: 8
    confidence: 0.95
  - name: wikilinks_obsidian
    weight: 7
    confidence: 0.9
  - name: estruturas_dados_obsidian
    weight: 8
    confidence: 0.92
  - name: canvas_obsidian
    weight: 7
    confidence: 0.93
  - name: ferramentas_linha_comando_obsidian
    weight: 6
    confidence: 0.88
  - name: extracao_conteudo_web
    weight: 7
    confidence: 0.94
  - name: organizacao_informacao_digital
    weight: 9
    confidence: 0.96
  - name: gerenciamento_contexto_vault
    weight: 6
    confidence: 0.85
  cdu_primary: '004.9'
  cdu_secondary:
  - '004.7'
  - '004.8'
  cdu_description: 004.9 - Tratamento de dados. Organização de dados. Gestão de dados. Armazenamento de dados. Recuperação de dados. Processamento de dados. 004.7 - Software. 004.8 - Inteligência artificial.
---
# Skills Instaladas

## Repositório Original
https://github.com/kepano/obsidian-skills

## Skills Disponíveis

| Skill | Descrição |
|-------|-----------|
| `obsidian-markdown/` | OFM: wikilinks, callouts, embeds, properties |
| `obsidian-bases/` | Bases (.base) com views, filtros, fórmulas |
| `json-canvas/` | Canvas (.canvas) com nós e conexões |
| `obsidian-cli/` | CLI para interacting com Obsidian |
| `defuddle/` | Extrair markdown limpo de páginas web |
| `vault-context/` | Contexto do seu vault Obsidian |

## Instalação

### defuddle (obrigatório para usar a skill)
```bash
npm install -g defuddle-cli
```

### Para ativar no opencode
Use: `/skill <nome-da-skill>` ou peça para ativar a skill desejada.

## Uso Recomendado

1. **Nova sessão**: Ativar `vault-context` primeiro
2. **Criar/editar notas**: Ativar `obsidian-markdown`
3. **Salvar artigos web**: Usar `defuddle` para limpar conteúdo
4. **Trabalhar com bases**: Ativar `obsidian-bases`
5. **Canvas**: Ativar `json-canvas`
