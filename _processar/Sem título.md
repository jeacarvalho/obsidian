---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T23:01:40.392381+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: classificacao_bibliografica
    weight: 10
    confidence: 0.98
  - name: classificacao_decimal_universal
    weight: 10
    confidence: 0.97
  - name: curadoria_conhecimento
    weight: 9
    confidence: 0.96
  - name: extracao_topicos
    weight: 8
    confidence: 0.94
  - name: sugestao_cdu
    weight: 8
    confidence: 0.93
  - name: formato_json
    weight: 7
    confidence: 0.92
  - name: regras_obrigatorias
    weight: 7
    confidence: 0.91
  - name: topicos_principais
    weight: 6
    confidence: 0.9
  - name: peso_topico
    weight: 6
    confidence: 0.89
  - name: confianca_topico
    weight: 5
    confidence: 0.88
  cdu_primary: '025.431'
  cdu_secondary: []
  cdu_description: Classificação Decimal Universal (CDU) para organização e recuperação de informação.
---
```dataview
TABLE 
    topic_classification.cdu_primary AS "CDU Principal",
    topic_classification.cdu_secondary AS "CDU Secundárias"
FROM ""
WHERE topic_classification.cdu_primary = "34"
SORT topic_classification.cdu_primary ASC