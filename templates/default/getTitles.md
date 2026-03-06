---
PromptInfo:
  promptId: getTitles
  name: 🗃️ Get Blog Titles
  description: select a content and list of blog titles will be generated
  author: Noureddine
  tags: writing
  version: 0.0.1
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:11.137714+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: geracao_titulos_blog
    weight: 10
    confidence: 0.98
  - name: escrita_conteudo
    weight: 9
    confidence: 0.95
  - name: marketing_digital
    weight: 8
    confidence: 0.9
  - name: criacao_conteudo
    weight: 8
    confidence: 0.92
  - name: redacao_persuasiva
    weight: 7
    confidence: 0.88
  - name: otimizacao_seo
    weight: 7
    confidence: 0.85
  - name: estrategia_conteudo
    weight: 6
    confidence: 0.8
  - name: ferramentas_escrita
    weight: 6
    confidence: 0.75
  - name: engajamento_leitor
    weight: 5
    confidence: 0.7
  - name: publicacao_online
    weight: 5
    confidence: 0.65
  cdu_primary: '004.77'
  cdu_secondary:
  - 004.774.2
  - '007.52'
  cdu_description: Comunicação eletrônica. Internet. World Wide Web. Publicação eletrônica. Criação de conteúdo para web.
---
content: 
{{context}}
prompt:
suggest 10 attractive blog titles about this content:

