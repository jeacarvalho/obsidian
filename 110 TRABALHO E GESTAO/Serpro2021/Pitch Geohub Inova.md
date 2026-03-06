---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:53.190575+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: geohub_infraestrutura_dados_georreferenciados
    weight: 10
    confidence: 0.98
  - name: geohub_automatizacao_coleta_dados
    weight: 9
    confidence: 0.95
  - name: geohub_osm_tiles_mirror_open_street_maps
    weight: 9
    confidence: 0.97
  - name: geohub_nominatim_mirror_consultas_osm
    weight: 9
    confidence: 0.97
  - name: geohub_nivel_servico_alto_uso
    weight: 8
    confidence: 0.96
  - name: geohub_centralizacao_dados
    weight: 8
    confidence: 0.94
  - name: geohub_atualizacao_automatizada_dados
    weight: 7
    confidence: 0.93
  - name: geohub_mecanismo_busca_atualizacao_sistemas
    weight: 7
    confidence: 0.92
  - name: geohub_mapas_base_georreferenciados
    weight: 6
    confidence: 0.9
  - name: geohub_dados_geograficos_serpro
    weight: 6
    confidence: 0.89
  cdu_primary: '004.27'
  cdu_secondary:
  - '004.65'
  - '004.77'
  - '911.2'
  cdu_description: Sistemas de informação. Gestão de dados. Bases de dados geográficas. Serviços de dados geográficos.
---
**Para** Clientes internos e externos **que** tenham necessidade de trabalhar com dados georeferenciados **o(a)** Geohub **é um(a)** infraestrutura para prover esses dados de maneira centralizada e automatizada **que** tem a possibilidade de automatizar a coleta de dados de seus fontes e fornecê-lo à sistemas que declarem a necessidade de uso desses dados **Diferente do(a)** desenvolvedor de cada sistema se responsabilizar pela atualização desses dados  **o produto** Geohub provê todo mecanismo de busca, atualização e sensibilização dos sistemas
**Autor:** José Eduardo 

**Para** Clientes internos e externos **que** tenham necessidade de trabalhar mapas base georeferenciados **o(a)** Geohub/osm tiles **é um(a)** Mirror do Open Street Maps disponibilizado na infraestrutura do [[serpro]] **que** provê os mesmos dados daquela organização, de maneira atualizada e com nível de serviço adequado ao ambiente do Serpro **Diferente do(a)** site do Open Street Maps, que não permite o uso massivo de consultas  **o produto** Geohub/osm tiles conta com nível de serviço que permite o alto uso 
**Autor:** José Eduardo 

**Para** Clientes internos e externos **que** tenham necessidade de trabalhar mapas base georeferenciados **o(a)** Geohub/Nominatim **é um(a)** Mirror da consulta fornecida pelo Open Street Maps disponibilizado na infraestrutura do Serpro **que** disponibiliza as mesmas consultas daquele site, em base local ao Serpro, atualizada, e com nível de serviço adequado ao ambiente da Empresa
**Diferente do(a)** nominatim no site do Open Street Maps, que não permite o uso massivo de consultas  **o produto** Geohub/nominatim conta com nível de serviço que permite o alto uso.
**Autor:** José Eduardo 