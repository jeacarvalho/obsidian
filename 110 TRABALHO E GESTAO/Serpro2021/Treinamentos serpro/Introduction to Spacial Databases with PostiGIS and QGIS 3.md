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


