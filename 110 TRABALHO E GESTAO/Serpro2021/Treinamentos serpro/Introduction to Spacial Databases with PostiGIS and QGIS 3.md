---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:59.936358+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: banco_de_dados_espaciais
    weight: 10
    confidence: 0.98
  - name: postgis
    weight: 10
    confidence: 0.99
  - name: qgis
    weight: 9
    confidence: 0.95
  - name: bibliotecas_open_source_geos
    weight: 7
    confidence: 0.9
  - name: bibliotecas_open_source_proj4
    weight: 7
    confidence: 0.9
  - name: bibliotecas_open_source_gdal
    weight: 7
    confidence: 0.9
  - name: bibliotecas_open_source_ogr
    weight: 7
    confidence: 0.9
  - name: instalacao_postgis
    weight: 8
    confidence: 0.97
  - name: gerenciamento_banco_dados_postgres
    weight: 8
    confidence: 0.96
  - name: importacao_shapefiles
    weight: 8
    confidence: 0.94
  cdu_primary: '004.25'
  cdu_secondary:
  - '528.9'
  - '551.4'
  cdu_description: Bancos de dados espaciais, sistemas de informação geográfica e geoprocessamento.
---
- Curso da udemy: https://www.udemy.com/course/introduction-to-spatial-databases-with-postgis-and-qgis/


## Aula 3 - What is a spatial database exactly?
- Open source libraries
	- GEOS
	- PROJ.4
	- GDAL
	- OGR

## Aula 4 - Where does a spatial database live?


Instalação do postgis

1. Segui orientação do site para instalar postgre
2. Alterei senha do usuário postgres
> sudo -i -u postgres
> psql
> \password postgres

4. POsteriormente, instalei a extensão pgis
> $ sudo add-apt-repository ppa:ubuntugis/ppa
$ sudo apt-get update
$ sudo apt-get install postgis 

5. instalei pgadmin4
6. Loguei como postgres
7. criei banco específico no servidor (nome "geo")
8. configurei extensão no novo banco (conforme https://stackoverflow.com/questions/24981784/how-do-i-add-postgis-to-postgresql-pgadmin)
> CREATE EXTENSION postgis
> CREATE EXTENSION postgis_topology;

9. Importação de shapefiles: 
> shp2pgsql -s SRID Raptor_Nests.shp | psql -h localhost -d curso_udemy -U ze


