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