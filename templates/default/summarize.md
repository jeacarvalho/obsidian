---
PromptInfo:
  promptId: summarize
  name: 🗞️ Summarize
  description: select a content and it will be summarized.
  author: Noureddine
  tags: writing, thinking, learning
  version: 0.0.1
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:10.793502+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: resumo_de_conteudo
    weight: 9
    confidence: 0.98
  - name: ferramenta_de_escrita
    weight: 8
    confidence: 0.95
  - name: processo_de_pensamento
    weight: 7
    confidence: 0.92
  - name: aprendizagem_automatica
    weight: 6
    confidence: 0.9
  - name: geracao_de_texto
    weight: 8
    confidence: 0.96
  - name: assistente_de_ia
    weight: 9
    confidence: 0.97
  - name: ferramenta_de_produtividade
    weight: 7
    confidence: 0.93
  - name: processamento_linguagem_natural
    weight: 6
    confidence: 0.88
  - name: criacao_de_conteudo
    weight: 8
    confidence: 0.94
  - name: otimizacao_de_texto
    weight: 7
    confidence: 0.91
  cdu_primary: '004.9'
  cdu_secondary:
  - '007'
  - '801.3'
  cdu_description: Processamento de informação. Sistemas de informação. Automação. Cibernética. Processamento de linguagem natural. Geração de texto. Resumo de conteúdo.
---
content: 
{{context}}
prompt:
summarize the content


