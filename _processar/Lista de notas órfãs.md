---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:41:32.833492+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: arquivos_sem_links
    weight: 10
    confidence: 0.98
  - name: arquivos_isolados
    weight: 9
    confidence: 0.97
  - name: arquivos_sem_referencias_externas
    weight: 8
    confidence: 0.96
  - name: arquivos_sem_referencias_internas
    weight: 8
    confidence: 0.96
  - name: gerenciamento_de_notas
    weight: 7
    confidence: 0.95
  - name: organizacao_de_informacoes
    weight: 7
    confidence: 0.94
  - name: estrutura_de_dados
    weight: 6
    confidence: 0.93
  - name: analise_de_grafos
    weight: 6
    confidence: 0.92
  - name: metadados_de_arquivos
    weight: 5
    confidence: 0.91
  - name: ferramentas_de_gerenciamento_de_conhecimento
    weight: 5
    confidence: 0.9
  cdu_primary: '004.6'
  cdu_secondary:
  - '025.431'
  cdu_description: Gerenciamento de dados e sistemas de informação, com foco em organização e classificação de informações.
---
``` dataview 
list from "" 
where length(file.inlinks) = 0 and length(file.outlinks) = 0 
```
