---
PromptInfo:
  promptId: getTags
  name: 🏷️Get Tags for Your Content
  description: Select a content and Get suggest Tags for it
  author: Noureddine
  tags: writing, learning
  version: 0.0.1
bodyParams:
  max_tokens: 30
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:11.193848+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: geracao_de_tags
    weight: 10
    confidence: 0.98
  - name: sugestao_de_tags
    weight: 9
    confidence: 0.97
  - name: ferramenta_de_escrita
    weight: 8
    confidence: 0.95
  - name: processamento_de_linguagem_natural
    weight: 7
    confidence: 0.92
  - name: aprendizado_de_maquina
    weight: 6
    confidence: 0.9
  - name: conteudo_digital
    weight: 5
    confidence: 0.88
  - name: otimizacao_de_conteudo
    weight: 7
    confidence: 0.93
  - name: criacao_de_conteudo
    weight: 8
    confidence: 0.96
  - name: analise_de_texto
    weight: 6
    confidence: 0.91
  - name: ferramenta_de_produtividade
    weight: 5
    confidence: 0.85
  cdu_primary: '004.9'
  cdu_secondary:
  - '800.9'
  - '006.3'
  cdu_description: Processamento de dados textuais, geração de texto, inteligência artificial aplicada à linguagem.
---
content: 
{{context}}
prompt:
suggest tags for the content in markdown format
tags:
