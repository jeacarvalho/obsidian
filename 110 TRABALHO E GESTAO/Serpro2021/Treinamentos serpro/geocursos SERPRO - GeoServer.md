---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:40:00.486623+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: padroes_ogc_webservices
    weight: 10
    confidence: 0.98
  - name: wms_web_map_service
    weight: 9
    confidence: 0.95
  - name: wcs_web_coverage_service
    weight: 8
    confidence: 0.92
  - name: geojson_padrao_substituto
    weight: 7
    confidence: 0.9
  - name: topojson_extensao_geojson
    weight: 6
    confidence: 0.88
  - name: sld_style_layer_description
    weight: 7
    confidence: 0.85
  - name: wfs_web_feature_service
    weight: 8
    confidence: 0.93
  - name: wps_web_process_service
    weight: 7
    confidence: 0.87
  - name: postgis_simple_feature_specification
    weight: 6
    confidence: 0.8
  - name: udig_criacao_estilo_camadas
    weight: 5
    confidence: 0.75
  cdu_primary: '004.6'
  cdu_secondary:
  - '004.77'
  - '528.9'
  cdu_description: Sistemas de informação geográfica, serviços web geográficos e padrões de intercâmbio de dados espaciais.
---
Link do curso: https://portaldoaluno.geocursos.com.br/videoAulaEAD.php?pCurso=48&pTurma=216

# Aula 02 - Padrões OGC
- https://portaldoaluno.geocursos.com.br/videoPlay.php?pHashVimeo=490556786&pCurso=48&pTurma=216
- São webservices com padrões determinados pela OGC
- Mais usados: WMS e WCS
- WMS (web map service), só imagem, sem atributos
- GeoJSON não é OGC mas vem substituindo os KML e GML
- TopoJSON - extensão do GeoJSON, mas com arquivos 80% menores
- SLD - Style Layer Description - no geoserver é um XML, mas pode ser usado css se plugin for utilizado
- WFS - Web feature service - recuperar objetos espaciais em GML (tem atributos)
- WCS - Web coverage service - fenômenos com variação contínua no espaço
- WPS - Web process service
	- Um português fez um projeto para encontrar menor caminho entre dois pontos com esse serviço
- SFS - Simple feature specification - PostGIS implementação de referência

#  Aula 02.01 - Acessando Serviços
- https://portaldoaluno.geocursos.com.br/videoPlay.php?pHashVimeo=490557692&pCurso=48&pTurma=216
- WMS não tem a opção de tabela de atributos quanto consumida no Qgis

# Aula 03 - Introdução e Instalação
- https://portaldoaluno.geocursos.com.br/videoPlay.php?pHashVimeo=490559014&pCurso=48&pTurma=216

# Aula 04 - Configuração
- https://portaldoaluno.geocursos.com.br/videoPlay.php?pHashVimeo=490561341&pCurso=48&pTurma=216

# Aula 08.01 - Instalação do uDig
- https://portaldoaluno.geocursos.com.br/videoPlay.php?pHashVimeo=490571197&pCurso=48&pTurma=216
- Ferramenta pra criar estilo de camadas
