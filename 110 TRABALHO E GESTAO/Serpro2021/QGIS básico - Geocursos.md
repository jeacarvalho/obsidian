---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:56.340155+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: historia_qgis
    weight: 7
    confidence: 0.85
  - name: pacotes_geoprocessamento_qgis
    weight: 8
    confidence: 0.9
  - name: uso_python_qgis
    weight: 6
    confidence: 0.75
  - name: conceito_raster
    weight: 7
    confidence: 0.8
  - name: ordem_camadas_qgis
    weight: 5
    confidence: 0.7
  - name: unir_fontes_dados_qgis
    weight: 8
    confidence: 0.92
  - name: estrutura_shapefile
    weight: 7
    confidence: 0.88
  - name: geopackage_dados_espaciais
    weight: 9
    confidence: 0.95
  - name: tendencia_geopackage
    weight: 8
    confidence: 0.9
  - name: ferramentas_analise_geo
    weight: 7
    confidence: 0.85
  cdu_primary: '528.9'
  cdu_secondary:
  - 004.456.3
  - '004.65'
  - '004.77'
  cdu_description: Geoprocessamento e Sistemas de Informação Geográfica (SIG), com foco em software (QGIS), formatos de dados (Shapefile, GeoPackage) e ferramentas de análise.
---
# Primeiro dia

## História do Qgis
- Junta vários pacotes para uso de GDAL, GEOS, Sqlite...
- Integração com pacotes opensource
- Usa python
- Raster = imagens, que são matrizes numéricas com valores de cores que compõe os pixels
- Ordem das camadas importa no Qgis
- É possível unir fontes de dados. Ter uma planilha com um monte de informação e unir com algum shapefile por algum campo comum

# Segundo dia
- Shapefiles = dbf (atributos), shp(geometrias), shx (ligação entre os dois)
- Join by nearest - juntando camadas
- Fix geometry - conserta alguns vértices errados
- Variáveis de report - @atlaspagename (exemplo)
- Tentar enviar mapa para [marcoaurelio.geoprocess@gmail.com](mailto:marcoaurelio.geoprocess@gmail.com)


# Terceiro dia

## Geopackages
- É um banco de dados. Tem tabelas
- vários layers
- é uma versão de um Sqlite
- é a tendência de dado espacial. Shapefiles tendem a perder sentido
- Camada, nova camada, geopackage
- "_l, _p, _a" --> Tipos de geometria de cada arquivo no package


# Quarto dia
## Ferramentas importantes para analista em geo
- Buffer
- Comando ctrl + alt +v --> Colar cópia como rascunho temporário
- 