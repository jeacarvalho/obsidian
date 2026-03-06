---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:10.849522+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: geracao_de_ideias
    weight: 9
    confidence: 0.9
  - name: brainstorming
    weight: 8
    confidence: 0.85
  - name: contexto_de_dados
    weight: 7
    confidence: 0.8
  - name: analise_de_texto
    weight: 6
    confidence: 0.75
  - name: processamento_linguagem_natural
    weight: 7
    confidence: 0.7
  - name: sistemas_de_ia
    weight: 8
    confidence: 0.88
  - name: ferramentas_de_desenvolvimento
    weight: 5
    confidence: 0.65
  - name: geracao_de_conteudo
    weight: 9
    confidence: 0.92
  - name: modelos_linguisticos
    weight: 7
    confidence: 0.78
  - name: testes_de_software
    weight: 6
    confidence: 0.72
  cdu_primary: '004.8'
  cdu_secondary:
  - '004.89'
  - '006.3'
  cdu_description: Inteligência artificial. Processamento de dados. Processamento de linguagem natural. Geração de texto.
---
---
Promptinfo:
	id: brainstormChildern
	name: Toro de parpites
	description:
	tags: testgenerator
	version: 0.0.1
___
context:
{{#each children}}
{{this.content}}
{{/each}}

prompt:
toro de parpites sobre o contexto
Ideas:
*