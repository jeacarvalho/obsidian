# Dados para acesso ao curso
>Oi José Eduardo Alves de Carvalho, tudo bem?
Por favor, confirme o recebimento deste email.
O email de suporte aos alunos é: alunos@clickgeo.com.br
Seguem abaixo seus dados de acesso ao curso:
Email: jose-eduardo.carvalho@[[serpro]].gov.br Senha: Dspx76mF
[Clique aqui para acessar o portal do aluno](https://mail-inspector.serpro.gov.br/mailinspector/tap/WarningUrlPage.php?HSCTYPE=0&HSCRULE=4&HSCID=RThGQjAzODcyRTYuQUU0QjA=&HSCMLICHECKID0005=b70b7db3446fb5c45272034c5174fcaa&URLCHECKHSCMLI09132012warnning=H4sIAAAAAAAAAwXB13aCMAAA0C+KDBmlbyEWigjIFHjpIRhZYYgpAl/vvTVj0+ub40hfNPRQEdaTHpO5a9ihHHuu5Mj5LbQz71U79CsZmNg6boEEa18mQJ8ncuqqs44SmKpabtNhkxxwW3LnjWyalwYW59weE0s7ubysWK2tJCEMbqIQ43Vsl6Zf6LUzLXwxSCgazC0aVU1XHUV+uMV9xpu1mtUGk/chDmYNu+GM/m1h+rJWna5DWO/RyoCsU1Kn9jN1PK0VDSoOQjT6DwWp6PULskKars+q6u7e40c+YnyJ/vAdtCaFOfwA99YrPf8AAAA=)
https://alunos.clickgeo.com.br/

Poderia nos enviar seu contato de WhatsApp ou telefone?
Ficamos à disposição.

# Livro sobre o tema:
- [[INTRODUÇÃO À CIÊNCIA DA GEOINFORMAÇÃO.pdf]]
- fonte: http://mtc-m12.sid.inpe.br/col/sid.inpe.br/sergio/2004/04.22.07.43/doc/publicacao.pdf

# 1.2. Geoprocessamento, Geotecnologias, SIG
- Arquivo da aula: [[1.2. Geoprocessamento, Geotecnologias, SIG.pdf]]
>Se "onde" é importante para o seu negócio então o geoprocessamento é sua ferramenta de trabalho - Câmara e Davis (2001)

## Algumas definições sobre o que é o geoprocessamento
>Conjunto de tecnologias voltadas a **coleta**, **armazenamento** e **tratamento** de informações espaciais para um objetivo específico. INPE, Manuais de geoprocessamento

>Geoprocessamento denota a disciplina de conhecimento que utiliza técnicas matemáticas e computacionais para o tratamento da informação geográfica - Livro geoprocessamento em projetos ambientais

- ![[DefinicoesGeoProcessamento.png]]

## SIG - Sistema de informações geográficas
- Conjunto de software, hardware, metodologias, recursos humanos e dados para processamento geográfico
- ![[ElementosSIG.png]]
- "se entra lixo, sai lixo" --> Atenção à qualidade dos dados

# 1.3. Visão Geral de Outras Geotecnologias 
- Arquivo da aula: [[1.3. Visão Geral de Outras Geotecnologias.pdf]]

## Fotogrametria
- Medição de distâncias por meio da fotografia
- Aerofotogrametria - imagens aéreas

### Ferramentas
- Aviões e drones

## Banco de dados geográficos
- Várias tabelas interligadas entre si
- Os dados são geográficos. O banco não é. Ele armazena dados geográficos e pode manipular/anaisar esses dados

### Ferramentas
- Postgis
- Oracle Spacial
- Mysql Spacial
- Geopackage
- SpatialLite

## WEBGIS
- Web mapping, mapa interativo disponível na internet. Exemplo google maps

### Ferramentas
- QGIS Cloud, MapServer, Geoserver, Openlayers, i3Geo

# 1.4. Softwares Livres e Geotecnologias
- Arquivo da aula:[[1.4. Softwares Livres e Geotecnologias.pdf]]
- SIG: 
	- Produção de mapas (Com relação a sistemas cartográficos)
	- Operações e análises de geoprocessamento
- Exemplos comerciais
	- Arcgis - um dos mais utilizados no mundoi
	- Mapainfo
	- Supergis
- Livres
	- Mais usados no Brasil atualmente: Qgis
	- GVSIG
	- Spring (Brasileiro)
	- Terravig (Brasileiro)
- Software livre - liberdade para:
	- Executar
	- Estudar o fonte
	- Modificar
	- Distribuir

# 1.5. Produtos Cartográficos
- Arquivo da aula: [[1.5. Produtos Cartográficos.pdf]]

## Mapa
- Representação do plano em **escala pequena**
- Território coberto por uma única folha
- Planificada
- Acidentes naturais e esquemas administrativos delimitam

## Carta
- Representação do plano em **escala média ou grande**
- Subdividida em folhas
- Planificada
- Limitadas por linhas convencionais
- Fazem parte de um mapa
- IBGE - loja IBGE - disponibiliza cartas

## Planta
- Espécie quarta
- - Representação do plano em **escala grande**
- Assim posso ver pequenas áreas e seus detalhes
- ![[EscalasMapaCartaPlanta.png]]

# [1.6 ESCALA](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108658-1-6-escala)
- Arquivo da aula: [[1.6. Escala.pdf]]
- Definição: Dimensões reais x representação no mapa. PROPORÇÃO

## Escalas numéricas
- Fraçao --> 1:25.000
	- 1 --> distância no mapa em centímetros
	- 25,000 --> distância na realidade
	- Nesse exemplo, cada centímento do mapa representa 25.000 centímetros da realidade
- Maior denominador menor a escala
- Quanto maior a escala mais detalhe. quanto menor a escala, menos detalhes
- Maior escala --> Menor área mapeada --> Mais informação --> menos generalização
	- Inverso tb é importante entender

## Erro e precisão gráfica
- Precisão gráfica percebida é de 0,2mm (0,0002 m) -- limitação do olho humano
- Multiplicar o denominador da escala por 0,0002 vai dar a precisão das medidas do mapa

 # [1.7 Sistema de Referência (DATUM e Coordenadas)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108660-1-7-sistema-de-referencia-datum-e-coordenadas)
  - DATUm + Sistema de coordenadas = Sistema de referência
  ## Datum
  - VErtical ou horizontal --> Modelo matemático de representação da superfície da Terra ao nível do mar, que não é uma esfera perfeita...
  -  DATUM oficial do Brasil desde de 2015 = SIRGAS 2000 ("AS" de América do Sul)
  ## Sistema de coordenadas (latitude / longitude)
  - UTM - unidades métricas
  - Geográficas/Geodésicas (grau decimal ou GMS)
  - Fusos - se área de interesse está totalmente abrangida em único fuso, tanto faz o uso de UTM ou GMS. Mas se área em mais de um fuso, UTM não é recomendado. UTM facilita cálculos métricos

  # [1.8 Códigos EPSG](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108660-1-7-sistema-de-referencia-datum-e-coordenadas)
  - Arquivo da aula: [[1.8. Códigos EPSG.pdf]]
  - EPSG - Grupo europeu de pesquisas de petróleo
  - Codificaram a junção de DATUM e coordenada

  # [1.9. Projeções Cartográficas Visão Geral](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108596-1-9-projecoes-cartograficas-visao-geral)
  - Arquivo da aula: [[1.9. Projeções Cartográficas Visão Geral.pdf]]
  - projeções tem como objetivo minimizar as distorções de "ver" um elemento esférico através de um plano

  ## Tipos de projeção
  - Plana, cônica e cilíndrica

  ## Propriedades de deformação
  - Conformes ou isogonais - mantém ângulos e formas; distorce tamanho
  - Isométricas / equivalentes- Conserva a área (medidas); distorce forma. Muitos consideram a melhor projeção para SIG
  - Equidistantes - Conserva as distâncias em determinadas direções

# [1.10. O Sistema UTM](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108664-1-10-o-sistema-utm)
- Arquivo da aula: [[1.10. Projeção UTM O Sistema UTM.pdf]]
- Projeção UTM <> Coordenada UTM
- Projeção Conforme/Isogonal

 # [1.11 Introdução aos Dados Geográficos](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108666-1-11-introducao-aos-dados-geograficos)
 - Arquivo da aula: [[1.11 Introdução aos Dados Geográficos.pdf]]
 - Shapefile, geopackage, etc...
 - Dado geográfico possui componente espacial: localização
	 - Lugar e tempo: horário ou data
	 - Atributo relacionado
 - Possibilidade de analisar interseção, sobreposição, etc...
 
 ## Classe vetorial
- Formato de coordenadas
- Que formam geometrias (ponto, linha ou área)
- Ocupam menos espaço por ter apenas coordenadas
- Mais fácil de armazenamento de BD
 - Principais formatos: shapeflle
	 - KML/KMZ (Google Earth)
	 - DWG/DGN - Cads
	 - DXF - cads (intercâmbio entre softwares)
	 - GPX (GPs...)
	 - Geopackage - deve substituir o shapefile --> Um banco de dados local
 
 ## Classe matricial (raster)
- Volumosos
- Principal: Imagens de satélite
	- Fotografias aéreas - aviões e drones
	- Modelos digitais de elevação
	- Geopackage

# [1.12. Formato Esri Shapefile (Shape)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108667-1-12-formato-esri-shapefile-shape)
- Arquivo da aula: [[1.12. Formato Esri Shapefile (Shape).pdf]]
- Existe tabela de atributos no arquivo
- Pode ter as 3 geometrias. Mas apenas um por shape
- é composto de múltiplos arquivos no sistema de arquivos, com várias extensões
	- Pelo menos 3 precisam existir para abrir corretamente: **SHP, DBF, SHX**
	- Outro arquivo muito importante: PRJ --> Aqui estão os sistemas de referências
- SHP --> Geometria do mapa
- DBF --> Tabela de atributos (até 10 caracteres para os nomes das colunas)
- SHX --> Junção do DBF e SHP
**- NÃO USE CARACTERES ESPECIAIS NO NOME DO ARQUIVO NEM NOS NOMES DOS CAMPOS DA TABELA**
- PRJ--> Sistema de referência 

# [1.13. Formato Geopackage](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108674-1-13-formato-geopackage)
- Arquivo da aula: [[1.13. Formato GeoPackage.pdf]]
- Formato aberto - Estrutura do Sqlite
- Extensão gpkg
- Dados + metadados (vetorias, raster e tabelas)
- www.geopackage.org

| Shapefile              | geopackage           |
| ---------------------- | -------------------- |
| Vários arquivos        | único arquivo        |
| geometria única        | Múltiplas geometrias |
| mázimo 2GB             | ilimitado            |
| nome coluna 10 caract. | sem limites          |
| 255 colunas            | 2000 colunas         |
| monousuário            | monousuário                     |


# [1.14. Formato de imagem](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108672-1-14-formato-de-imagem)
- Arquivo da aula: [[1.14. Formato de imagem.pdf]]
- Conceitos de dados raster
- 4 tipos de resolução: Espacial, Temporal, Radiométrica e espectral

## Espacial
- Tamanho do lado do pixel
- Esse tamanho indica o tamanho do menor objeto identificado
- Maior tamanho pixel = menor resolução

## Temporal
- Período de revisita - tempo que o satélite retorna ao mesmo local

## Radiométrica
- níveis de cinza de registro da imagem
- número de bits da imagem diz isso.

## Espectral
- Sensores multiespectral
- ![[EspectrosEletromagneticos.png]]

## Satélites com imagens gratuitas
- LANDSAT (desde década 70) - 30 m resolução espacial
- CBERS (China Brasil) -  20 mt
- SENTINEL-2 - 10 mt, cinco dias de revista

## Modelos digitais de elevação (MDE)
- No pixel está armazenada a cota.
- MDT - Terreno
- MDS - Superfície (pega os objetos.. casas, etc...)
- SRTM - Imagens do ônibus espacial com 30 mt de resolução, liberadas em 2014 por Obama
- ALOS PALSAR (Japão) - 12,5 mt de resolução!
- ASTER GDEM - 30 mt, mais recentes.

# [1.15. Outros Formatos de Dados Geográficos](https://alunos.clickgeo.com.br/872-metodo-geo-pro/135344-1-15-outros-formatos-de-dados-geograficos)
- Arquivo da aula: [[1.15. Outros Formatos de Dados Geográficos.pdf]]
- OGC - Consórcio geoespacial aberto


# [1.16 Onde encontrar Dados Geográficos](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108673-1-16-onde-encontrar-dados-geograficos)
- Arquivo da aula: [[1.16 Onde encontrar Dados Geográficos.pdf]]

# [2.1 O Projeto QGIS](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108606-2-1-o-projeto-qgis)
- Arquivo da aula: [[2.1. O Projeto QGIS.pdf]]

# [2.2. Linhas de Desenvolvimento do QGIS e Instalação](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108607-2-2-linhas-de-desenvolvimento-do-qgis-e-instalacao)
- Arquivo da aula: [[2.2. Linhas de Desenvolvimento do QGIS e Instalação.pdf]]
- LTR é a versão recomendada
- LR versão de testes

# [2.3 Instalação Básica do QGIS](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108976-2-3-instalacao-basica-do-qgis)
- Arquivo da aula: [[2.3. Instalação do Software QGIS.pdf]]

# [2.4 Instalação Avançada](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108977-2-4-instalacao-avancada)
- Arquivo da aula: [[2.4. Instalação Avançada.pdf]]

# [2.5. Download: Dados Geográficos para as Aulas](https://alunos.clickgeo.com.br/872-metodo-geo-pro/135382-2-5-download-dados-geograficos-para-as-aulas)
- Arquivo da aula: [[2.5. Download_ Dados Geográficos para as Aulas.pdf]]

# [2.6. Recomendações Importantes para Uso Correto do QGIS](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108610-2-6-recomendacoes-importantes-para-uso-correto-do-qgis)
- Arquivo aula: [[2.6. Recomendações Importantes para Uso Correto do QGIS.pdf]]

# [2.7. Conhecendo a Interface do QGIS](https://alunos.clickgeo.com.br/872-metodo-geo-pro/108611-2-7-conhecendo-a-interface-do-qgis)
- Arquivo aula: [[2.7. Conhecendo a Interface do QGIS.pdf]]

# [2.8 Como Iniciar Projetos no Software QGIS](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109116-2-8-como-iniciar-projetos-no-software-qgis)
- Arquivo aula: [[2.8 Como Iniciar Projetos no Software QGIS.pdf]]
- 1a coisa: sistema de referência!

# [2.9. Introdução a Seleção e Consulta de Dados em SIG](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109117-2-9-introducao-a-selecao-e-consulta-de-dados-em-sig)
- Arquivo aula: [[2.9. Introdução a Seleção e Consulta de Dados em SIG.pdf]]

# [2.10. Seleção Manual](https://alunos.clickgeo.com.br/872-metodo-geo-pro/112036-2-10-selecao-manual)
- Arquivo aula: [[2.10. Seleção Manual.pdf]]

# [2.11. Seleção por Localização](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109052-2-11-selecao-por-localizacao)
- Arquivo aula: [[2.11. Seleção por Localização.pdf]]

# [2.12. Seleção por Expressões (Parte 1)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109178-2-12-selecao-por-expressoes-parte-1)
- Arquivo aula: [[2.12. Seleção por Expressões (Parte 1).pdf]]

# [2.13. Seleção por Expressões (Parte 2)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109179-2-13-selecao-por-expressoes-parte-2)
- Arquivo aula: [[2.13. Seleção por Expressões (Parte 2).pdf]]

# [3.1. Simbolização Cartográfica (Conceitos)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/197273-3-1-simbolizacao-cartografica-conceitos)
- Arquivo aula: [[3.1. Simbolização Cartográfica (Conceitos).pdf]]

## Semiologia gráfica
- Simbolização de dados espaciais nos produtos cartográficos. 

# [3.2 Criando um Shapefile Manualmente](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109215-3-2-criando-um-shapefile-manualmente)
- Arquivo aula: [[3.2. Criando um Shapefile Manualmente.pdf]]
- Shapefile só tem tipo "CHAR" de dados texto
- SHP com linha precisa ter cuidado com a escala. Manter igual sempre enquanto criando as linhas. OU seja se mudar o zoom tem que voltar a escala inicial

# [3.3. Simbologia no QGIS (SVG)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109216-3-3-simbologia-no-qgis-svg)
- Arquivo aula: [[3.3. Simbologia no QGIS (SVG).pdf]]

# [3.4 Simbologia no QGIS (QML)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109217-3-4-simbologia-no-qgis-qml)
- Arquivo aula: [[3.4. Simbologia no QGIS (QML).pdf]]
- salvar simbologias criadas em um mapa para uso em outros. Estilos, importar, salvar nas propriedades da camada

# [3.5. Dicas para Escolha de Cores para Mapas](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109218-3-5-dicas-para-escolha-de-cores-para-mapas)
- Arquivo aula: [[3.5. Dicas para Escolha de Cores para Mapas.pdf]]
- colorbrewer.org

# [3.6. Toponímia - Rotulação (Etiquetas)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109223-3-6-toponimia-rotulacao-etiquetas)
- Arquivo aula: [[3.6. Toponímia - Rotulação (Etiquetas).pdf]]
- Textos que aparecem nos mapas para descrever o que está sendo mapeado
- rotulação, etiquetas

# [3.7. Introdução aos Mapas Temáticos](https://alunos.clickgeo.com.br/872-metodo-geo-pro/109219-3-7-introducao-aos-mapas-tematicos)
- Arquivo aula: [[3.7. Introdução aos Mapas Temáticos.pdf]]
- tipos: qualitativo, quantitativo, baseado em regras
- QGIS: mapa categorizado

# [3.8. Como Unir Tabelas de Dados com Mapas (Join)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/111526-3-8-como-unir-tabelas-de-dados-com-mapas-join)
- Arquivo aula: [[3.8. Como Unir Tabelas de Dados com Mapas (Join).pdf]]

# [3.9 Mapas Qualitativos (Categorizados)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/111318-3-9-mapas-qualitativos-categorizados)
- Arquivo aula: [[3.9. Mapas Qualitativos (Categorizados).pdf]]

# [3.10. Mapas Quantitativos (Graduados)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/111469-3-10-mapas-quantitativos-graduados)
- Arquivo aula: [[3.10. Mapas Quantitativos (Graduados).pdf]]


# [3.11. Mapas Baseados em Regras](https://alunos.clickgeo.com.br/872-metodo-geo-pro/111527-3-11-mapas-baseados-em-regra)
- Arquivo aula: [[3.11. Mapas Baseados em Regra.pdf]]

# [3.12. Mapas de Símbolos Pontuais Proporcionais](https://alunos.clickgeo.com.br/872-metodo-geo-pro/115324-3-12-mapas-de-simbolos-pontuais-proporcionais)
- Arquivo aula: [[3.12. Mapas de Símbolos Pontuais Proporcionais.pdf]]

# [3.13. Mapas de Fluxo](https://alunos.clickgeo.com.br/872-metodo-geo-pro/197014-3-13-mapas-de-fluxo)
- Arquivo aula: [[3.13. Mapas de Fluxo.pdf]]

# [4.1. Complementos, Camadas e Cálculos Métricos](https://alunos.clickgeo.com.br/872-metodo-geo-pro/115325-4-1-complementos-camadas-e-calculos-metricos)
- Arquivo aula: [[4.1. Complementos, Camadas e Cálculos Métricos.pdf]]

# [4.2. Instalação de Complementos (Plugins)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/112035-4-2-instalacao-de-complementos-plugins)
- Arquivo aula: [[4.2. Instalação de Complementos (Plugins).pdf]]
- Autosaver

# [4.3. Validação e Correção de Erros Topológicos](https://alunos.clickgeo.com.br/872-metodo-geo-pro/115326-4-3-validacao-e-correcao-de-erros-topologicos)
- Arquivo aula: [[4.3. Validação e Correção de Erros Topológicos.pdf]]
- Topology checker, editar camada, selecionar, mover, excluir, checar novamente

# [4.4. Ferramentas de Ajuste, Edição e Precisão](https://alunos.clickgeo.com.br/872-metodo-geo-pro/137306-4-4-ferramentas-de-ajuste-edicao-e-precisao)
- Arquivo aula: [[4.4. Ferramentas de Ajuste, Edição e Precisão.pdf]]

# [4.5. Criar camada Pontual a partir de Coordenadas (Parte 1)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/118402-4-5-criar-camada-pontual-a-partir-de-coordenadas-parte-1)
- Arquivo aula: [[4.5. Criar camada Pontual a partir de Coordenadas (Parte 1).pdf]]
- Importar um csv. Deu trabalho para não errar no DATUM / sistema de coordenadas

# [4.6. Criar camada Pontual a partir de Coordenadas (Parte 2)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/118403-4-6-criar-camada-pontual-a-partir-de-coordenadas-parte-2)
- Arquivo aula: [[4.6. Criar camada Pontual a partir de Coordenadas (Parte 2).pdf]]
- Latlon plugin e digitar coordenadas "na mão"

# [4.7. Como Obter (extrair) Coordenadas](https://alunos.clickgeo.com.br/872-metodo-geo-pro/118404-4-7-como-obter-extrair-coordenadas)
- Arquivo aula: [[4.7. Como Obter (extrair) Coordenadas.pdf]]

# [4.8. Conversão de Geometrias](https://alunos.clickgeo.com.br/872-metodo-geo-pro/118405-4-8-conversao-de-geometrias)
- Arquivo aula: [[4.8. Conversão de Geometrias.pdf]]

# [4.9. Cálculo de Áreas, Distância e Perímetros (Parte 1)]
- Arquivo aula: [[4.9. Cálculo de Áreas, Distância e Perímetros (Parte 1).pdf]]

# [4.10. Cálculo de Áreas, Distâncias e Perímetros (Parte 2)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/118407-4-10-calculo-de-areas-distancias-e-perimetros-parte-2)
- Arquivo aula: [[4.10. Cálculo de Áreas, Distâncias e Perímetros (Parte 2).pdf]]

![[GEoProNaoAula411.png]]

# [4.12. Calculadora de Campos - Expressões Condicionais](https://alunos.clickgeo.com.br/872-metodo-geo-pro/123311-4-12-calculadora-de-campos-expressoes-condicionais)
- Arquivo aula: [[4.12. Calculadora de Campos - Expressões Condicionais.pdf]]

# [4.13. Calculadora de Campos - Concatenação de Campos de Texto (String)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/123312-4-13-calculadora-de-campos-concatenacao-de-campos-de-texto-string)
- Arquivo aula: [[4.13. Calculadora de Campos - Concatenação de Campos de Texto (String).pdf]]

# [4.14. Calculadora de Campos - Outros recursos importantes](https://alunos.clickgeo.com.br/872-metodo-geo-pro/123458-4-14-calculadora-de-campos-outros-recursos-importantes)
- Arquivo aula: [[4.14. Calculadora de Campos - Outros recursos importantes.pdf]]

# [4.15. Criação de Polígonos usando Azimute e Distância](https://alunos.clickgeo.com.br/872-metodo-geo-pro/119886-4-15-criacao-de-poligonos-usando-azimute-e-distancia)
- Arquivo aula: [[4.15. Criação de Polígonos usando Azimute e Distância.pdf]]

# [4.16. Geração de Memorial Descritivo](https://alunos.clickgeo.com.br/872-metodo-geo-pro/119887-4-16-geracao-de-memorial-descritivo)
- Arquivo aula: [[4.16. Geração de Memorial Descritivo.pdf]]
- Memorial descritivo = documento formal para mapear uma propriedade

# [4.17. Criação e Configuração de Hiperlinks](https://alunos.clickgeo.com.br/872-metodo-geo-pro/123057-4-17-criacao-e-configuracao-de-hiperlinks)
- Arquivo aula: [[4.17. Criação e Configuração de Hiperlinks.pdf]]

# [4.18. Ferramentas GPS](https://alunos.clickgeo.com.br/872-metodo-geo-pro/134242-4-18-ferramentas-gps)
- Arquivo aula: [[4.18. Ferramentas GPS.pdf]]


# [5.1. Introdução à Análise Espacial de Dados Geográficos](https://alunos.clickgeo.com.br/872-metodo-geo-pro/123913-5-1-introducao-a-analise-espacial-de-dados-geograficos)
- Arquivo aula: [[5.1. Introdução à Análise Espacial de Dados Geográficos.pdf]]
- Livro do INPE análise espacial de dados geográficos: http://www.dpi.inpe.br/gilberto/livro/analise/

# [5.2. Buffer](https://alunos.clickgeo.com.br/872-metodo-geo-pro/123933-5-2-buffer)
- Arquivo aula: [[5.2. Buffer.pdf]]

# [5.3. Dissolve (Agregação)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/124307-5-3-dissolve-agregacao)
- Arquivo aula: [[5.3. Dissolve (Agregação).pdf]]

# [5.4. Separação de Feições](https://alunos.clickgeo.com.br/872-metodo-geo-pro/124308-5-4-separacao-de-feicoes)
- Arquivo aula: [[5.4. Separação de Feições.pdf]]

# [5.5. União de Feições (Merge)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/124309-5-5-uniao-de-feicoes-merge)
- Arquivo aula: [[5.5. União de Feições (Merge).pdf]]

# [5.6. Recorte de Camadas Vetoriais]
- Arquivo aula: [[5.6. Recorte de Camadas Vetoriais.pdf]]

# [5.7. Intersecção de Camadas](https://alunos.clickgeo.com.br/872-metodo-geo-pro/159821-5-7-interseccao-de-camadas)
- Arquivo aula: [[5.7. Intersecção de Camadas.pdf]]

# [6.1. Preparando o Mapa para Impressão (Parte 1)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/137308-6-1-preparando-o-mapa-para-impressao-parte-1)
- Arquivo aula: [[6.1. Preparando o Mapa para Impressão (Parte 1).pdf]]

# [6.2. Preparando o Mapa para Impressão (Parte 2)](https://alunos.clickgeo.com.br/872-metodo-geo-pro/137309-6-2-preparando-o-mapa-para-impressao-parte-2)
- Arquivo aula: [[6.2. Preparando o Mapa para Impressão (Parte 2).pdf]]


# [7.1. Principais Conceitos de Sensoriamento Remoto](https://alunos.clickgeo.com.br/872-metodo-geo-pro/197341-7-1-principais-conceitos-de-sensoriamento-remoto)
- Arquivo aula: [[7.1. Principais Conceitos de Sensoriamento Remoto.pdf]]

# [7.2. Georreferenciamento de Imagens](https://alunos.clickgeo.com.br/872-metodo-geo-pro/124676-7-2-georreferenciamento-de-imagens)
- Arquivo aula: [[7.2. Georreferenciamento de Imagens.pdf]]

# [7.3. Conversão de DN para Reflectância para gerar NDVI](https://alunos.clickgeo.com.br/872-metodo-geo-pro/212576-7-3-conversao-de-dn-para-reflectancia-para-gerar-ndvi)
- Arquivo aula: [[7.3. Conversão de DN para Reflectância para gerar NDVI.pdf]]

# [7.5. Mosaico de Imagens](https://alunos.clickgeo.com.br/872-metodo-geo-pro/125498-7-5-mosaico-de-imagens)
- Arquivo aula: [[7.5. Mosaico de Imagens.pdf]]

# [7.6. Recorte de Dados Raster]
- Arquivo aula: [[7.6. Recorte de Dados Raster.pdf]]

# [7.7. Geração de Composição Colorida](https://alunos.clickgeo.com.br/872-metodo-geo-pro/125500-7-7-geracao-de-composicao-colorida)
- Arquivo aula: [[7.7. Geração de Composição Colorida.pdf]]

# [7.8. Extração de Bandas Espectrais](https://alunos.clickgeo.com.br/872-metodo-geo-pro/125501-7-8-extracao-de-bandas-espectrais)
- Arquivo aula: [[7.6. Recorte de Dados Raster.pdf]]

# [8.1. Consumindo serviços OGC - WMS, WFS e WCS](https://alunos.clickgeo.com.br/872-metodo-geo-pro/201659-8-1-consumindo-servicos-ogc-wms-wfs-e-wcs)
- Arquivo aula: [[8.1. Consumindo serviços OGC - WMS, WFS e WCS.pdf]]
- WMS, WFS e WCS --> Webservices geográfricos
	- WMS - Map (apenas a imagem)
	- WFS - Feition (dados vetoriais)
	- WCS - Coverage (raster)
	- INDE : https://www.inde.gov.br/CatalogoGeoservicos

# [8.2. Uso de Base Maps - QuickMapServices e OpenLayers Plugin](https://alunos.clickgeo.com.br/872-metodo-geo-pro/139154-8-2-uso-de-base-maps-quickmapservices-e-openlayers-plugin)
- Arquivo aula: [[8.2. Uso de Base Maps - QuickMapServices e OpenLayers Plugin.pdf]]

# [8.3. Como Publicar Mapas Interativos na Internet - Parte 1](https://alunos.clickgeo.com.br/872-metodo-geo-pro/204309-8-3-como-publicar-mapas-interativos-na-internet-parte-1)
- Arquivo aula: [[8.3. Como Publicar Mapas Interativos na Internet - Parte 1.pdf]]

# [8.4. Como Publicar Mapas Interativos na Internet - Parte 2](https://alunos.clickgeo.com.br/872-metodo-geo-pro/216756-8-4-como-publicar-mapas-interativos-na-internet-parte-2)
-Arquivo aula: [[8.4. Como Publicar Mapas Interativos na Internet - Parte 2.pdf]]

# [8.5. Geocodificação de Endereços](https://alunos.clickgeo.com.br/872-metodo-geo-pro/216757-8-5-geocodificacao-de-enderecos)
- Arquivo aula: [[8.5. Geocodificação de Endereços.pdf]]

# [9.1. O que é um Banco de Dados Geográficos]
- Arquivo aula: [[9.1. O que é um Banco de Dados Geográficos.pdf]]

# [9.2. PostgreSQL, PostGIS e PgAdmin](https://alunos.clickgeo.com.br/872-metodo-geo-pro/137314-9-2-postgresql-postgis-e-pgadmin)
- Arquivo aula: [[9.2. PostgreSQL, PostGIS e PgAdmin.pdf]]

# [9.3. Shapefiles x Banco de Dados Geográficos](https://alunos.clickgeo.com.br/872-metodo-geo-pro/137716-9-3-shapefiles-x-banco-de-dados-geograficos)
- Arquivo aula: [[9.3. Shapefiles x Banco de Dados Geográficos.pdf]]

# [9.5. Criação de um Banco de Dados](https://alunos.clickgeo.com.br/872-metodo-geo-pro/137889-9-5-criacao-de-um-banco-de-dados)
- Arquivo aula: [[9.5. Criação de um Banco de Dados.pdf]]

# [9.6. Como Importar dados para o PostGIS - Parte 1](https://alunos.clickgeo.com.br/872-metodo-geo-pro/137932-9-6-como-importar-dados-para-o-postgis-parte-1)
- Arquivo aula: [[9.6. Como Importar dados para o PostGIS - Parte 1.pdf]]

# [9.7. Como Importar dados para o PostGIS - Parte 2](https://alunos.clickgeo.com.br/872-metodo-geo-pro/137933-9-7-como-importar-dados-para-o-postgis-parte-2)
- Arquivo aula: [[9.7. Como Importar dados para o PostGIS - Parte 2.pdf]]

# [9.8. Integração do QGIS com PostGIS](https://alunos.clickgeo.com.br/872-metodo-geo-pro/138303-9-8-integracao-do-qgis-com-postgis)
- Arquivo aula: [[9.8. Integração do QGIS com PostGIS.pdf]]

# [9.9. Práticas com GeoPackage]
- Arquivo aula: [[9.9. Práticas com GeoPackage.pdf]]

