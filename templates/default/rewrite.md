---
PromptInfo:
  promptId: rewrite
  name: ✏️ Rewrite, Paraphrase
  description: select a content and it will be rewriten.
  author: Noureddine
  tags: writing
  version: 0.0.1
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:10.993961+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: reescrita_de_conteudo
    weight: 10
    confidence: 0.98
  - name: parafrase_textual
    weight: 9
    confidence: 0.97
  - name: melhoria_de_escrita
    weight: 8
    confidence: 0.96
  - name: tornar_texto_atraente
    weight: 7
    confidence: 0.95
  - name: ferramenta_de_escrita
    weight: 6
    confidence: 0.94
  - name: geracao_de_texto
    weight: 5
    confidence: 0.93
  - name: otimizacao_de_conteudo
    weight: 7
    confidence: 0.92
  - name: engajamento_do_leitor
    weight: 6
    confidence: 0.91
  - name: criatividade_na_escrita
    weight: 5
    confidence: 0.9
  - name: processamento_linguagem_natural
    weight: 5
    confidence: 0.89
  cdu_primary: '808.1'
  cdu_secondary:
  - '004.77'
  - '415'
  cdu_description: Estilística e retórica; Linguagem e estilos de escrita; Processamento de linguagem natural e inteligência artificial aplicada à escrita.
---
content: 
{{context}}
prompt:
rewrite the content to make it more attractive
