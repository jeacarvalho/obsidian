---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:59.266737+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: geoprocessamento_qgis
    weight: 9
    confidence: 0.98
  - name: geoprocessamento_geoserver
    weight: 8
    confidence: 0.97
  - name: geoprocessamento_geotools
    weight: 7
    confidence: 0.96
  - name: banco_de_dados_postgis
    weight: 10
    confidence: 0.99
  - name: otimizacao_postgresql
    weight: 9
    confidence: 0.98
  - name: configuracao_postgresql_conf
    weight: 8
    confidence: 0.97
  - name: parametros_shared_buffers
    weight: 7
    confidence: 0.96
  - name: parametros_work_mem
    weight: 6
    confidence: 0.95
  - name: parametros_wal_buffers
    weight: 5
    confidence: 0.94
  - name: parametros_checkpoint_segments
    weight: 5
    confidence: 0.93
  cdu_primary: '004.89'
  cdu_secondary:
  - '004.65'
  - '004.77'
  cdu_description: Sistemas de informação geográfica (004.89), com foco em software de geoprocessamento (QGIS, GeoServer, GeoTools) e otimização de bancos de dados espaciais (PostGIS, PostgreSQL).
---
[[geocursos SERPRO - Módulo geotools]]
[[QGIS básico - Geocursos]]
[[geocursos SERPRO - GeoServer]]

# Postgis tunning
## arquivo postgresql.conf
- Shared buffer: 75% da memória da máquina
- Work men (? deve ser mem): 16mb
- maintenance work mem: 16 mb
- wal buffers: 1mb
- checkpoints segments: 6
- random page cost: 2.0
- seq page cost: 1.0