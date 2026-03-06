---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:26.930800+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: consulta_tabela_dataview
    weight: 8
    confidence: 0.9
  - name: filtragem_por_data_modificacao
    weight: 9
    confidence: 0.92
  - name: ordenacao_por_data_modificacao
    weight: 7
    confidence: 0.88
  - name: exclusao_diretorio_especifico
    weight: 6
    confidence: 0.85
  - name: linguagem_dataview
    weight: 10
    confidence: 0.98
  - name: metadados_arquivo
    weight: 7
    confidence: 0.87
  - name: consulta_arquivos_recentes
    weight: 9
    confidence: 0.93
  - name: intervalo_datas_especifico
    weight: 8
    confidence: 0.91
  - name: sintaxe_dataview
    weight: 10
    confidence: 0.97
  - name: visualizacao_tabela
    weight: 6
    confidence: 0.86
  cdu_primary: '004.6'
  cdu_secondary:
  - '025.431'
  cdu_description: Gestão de dados e bases de dados; Sistemas de informação; Organização do conhecimento; Classificação Decimal Universal
---
```dataview
TABLE file.mtime FROM -"99 TRABALHO E GESTAO/Serpro2021"
WHERE file.mtime >= (date("2025-01-26")) and file.mtime < (date("2025-01-30") + dur(1 day)) 
SORT file.mtime asc
