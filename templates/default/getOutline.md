---
PromptInfo:
  promptId: getOutline
  name: 🗒️Generate Outline
  description: Select a title, an outline will be generated for You.
  required_values: title
  author: Noureddine
  tags: writing
  version: 0.0.1
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:10.707228+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: geracao_de_conteudo
    weight: 9
    confidence: 0.98
  - name: estruturacao_de_texto
    weight: 8
    confidence: 0.95
  - name: redacao_para_blogs
    weight: 10
    confidence: 0.99
  - name: ferramentas_de_escrita
    weight: 7
    confidence: 0.9
  - name: criacao_de_esquemas
    weight: 8
    confidence: 0.96
  - name: otimizacao_de_prompts
    weight: 7
    confidence: 0.92
  - name: escrita_automatizada
    weight: 6
    confidence: 0.85
  - name: planejamento_editorial
    weight: 7
    confidence: 0.91
  - name: geracao_de_ideias
    weight: 8
    confidence: 0.94
  - name: assistentes_virtuais_de_escrita
    weight: 6
    confidence: 0.88
  cdu_primary: '808.1'
  cdu_secondary:
  - '004.777'
  - '801.7'
  cdu_description: Redação, retórica, estilo. Redação para publicações periódicas. Processamento de texto por computador.
---
title:
{{title}}
prompt:
write an outline for a blog for this title.
outline:
- 