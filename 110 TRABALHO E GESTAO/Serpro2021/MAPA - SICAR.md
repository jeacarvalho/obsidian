# Descrição:

Absorção do sistema [SICAR](https://www.car.gov.br/#/sobre) 


| links                                                                                                      | Arquivos |
| ---------------------------------------------------------------------------------------------------------- | -------- |
| [pasta drive com documentos](https://drive.google.com/drive/u/1/folders/1NWBlg28-HVN9KacdyYSiPaufCvmIqB7J) |          |
|                                                                                                            |          |

___
# 20230526 Sisflora, apresentação mesmo time de ontem da Tecnomapas
- Sisflora 2 --> Rastreabilidade da madeira
- 

___
# 20230525 Apresentação do Simcar MT
- Mapa? MMA?
- Mémora - Empresa que veio ao [[serpro]] apresentar uma possibilidade de parceria?
- Tecnomapas é a empresa responsável.
- SIMCAR e não SICAR!
	- Substituiu o Car federal em Mato Grosso
	- Tem paridade com Sicar
- Oracle Spatial
- Cruza cada tentativa de envio de mapa que usuário cria com as reservas, etc... Se tá válido o arquivo, se todos os dados foram informados, etc... É um processamento de malha na entrada
- mapadocar.com.br --> Mapas gratuitos que são disponibilizados gratuitamente para que o usuário pode usar para melhores mapas para usar no Car
- 

___
# 20210716 - Jonas
- Operação apenas no Serpro, multicloud

___
# 20210305 - 2a reunião Cadastro ambiental Rural - SICAR /MAPA
##### Infra, HEPTA
- Cloud first? AWS - Fernando Moreli e Kevin Lira (Fabio Correa Link?)
- Hepta - Arquitetura do Datacenter (Paulo Oliveira)
	- CISCO UCS - 2 sockets 44 CPUS - ![[InfraSICAR.png]]
	- Gitlab para versionamento dos fontes. Mas não está em funcionamento CI/CD
	- Conectividade:
		- ![[ConectividadeSICAR.png]]
		- ZerumLinx - Análise de vulnerabilidades
		- Teve issue para correção? Algum aberto?
			- Apenas de infra, não códigos. Mas todas ou quase todas resolvidas.
	- Monitoração
		- Sincronismo com estados é monitorado.
		- Ferramentas: Zabbix e  grafana
	- Links internet: Telebrás - 100MB
	- BD
		- Clusterizado com pgpool em produção - 2 instâncias
		- 3a instância para consultas, pelo que entendi.
		- Postgres 9.2
	- Sala segura no ambiente do Ibama - Bloco H
	- Storages - discos SATAs.
		- Ficou meio confuso, mas parece haver um desejo de que algumas partes dos sistemas estejam em SSD, como o banco, por exemplo. Isaias, desenvolvimento, confirmou esse entendimento posteriormente
	- Carga do sistema - usuários simultâneos? COnsumo de rede (não tem de pronto no momento, mas é possível levantar)

##### - Ufla  - PEdro Diniz Magalhães
- Desenvolvimento, suporte do sistema, Adm do BD, Adm. Mq. virtuais
- 18 módulos em produção
	- Tec. livres na maior parte
	- Java 7, 8 e 11
	- Play Springboot
	- JS...Angular, vue e react
	- Geoserver
	- Docker (sem k8s pelo que entendi da última reunião)
	- CentOs 7
	- Pg 9.2 e Postgis 1.5.8
- BD : 2,5TB
- Arquivos: 
	- 6 TB de arquivos recepctionados (.car)
	- PDFs
	- Imagens [RapidEye](http://www.dgi.inpe.br/documentacao/satelites/rapideye) [Outra referência](https://pt.wikipedia.org/wiki/RapidEye) - via NGINX
- Arquitetura: ![[ArquiteturaMAPA_SICAR.png]]
- 720 mil acessos ao site principal www.car.gov.br
- 1.6 milhões de usuários
	- 7 milhões de imóveis cadastrados

##### Imagem - Anderson Santos
- Ficamos sem horário. Será reagendado
- 

___
# 20210226 - Reunião inicial SICAR/MAPA
- Flavio Scofano diretor do MAPA responsável pelo sistema do CAR
	- Rejane
- Luca  TI ZETA
	- Herbert
	- Isaias
	- PEdro Magalhães
	- Ronan - grupo Imagen
	- Welington
	- Mateus
- TI MAPA - Bruno Hahn
- TI Min. Economia - Heverton

##### Contextualização
- SERPRO em reunião anterior sentiu necessidade de chamar o time de TI
- Bruno, contexto:
	- Trazer SICAR para dentro da infra do SERPRO

##### Apresentação do sistema
Linguagem
- Java
	- Diferentes versões. Quais?
	- [Play framework](https://en.wikipedia.org/wiki/Play_Framework)
	- Spring boot
- Scala

- Conteinerizado com Docker, não orquestrado por K8s
- 

ArcGIS
- Usa vário insumos carregados no GeoDatabase do ArcGis
- Tem tb alguns shapefiles

Banco: POstgres (qual versão) com postgis

Frontend: Angular e vue.js
	Outros para componentes - Quais?


GeoServer com Jetty embutido

Tudo é tecnologia livre. menos o Java
- Openjdk não se mostrou performática ou eficiente em algumas coisas
- Java 7 da Oracle
- Receptor ainda com Java "velho"

Várias aplicações


**Estrutura**
SICAR - Declaração de imóvel Rural
Base - 6 milhões de cadastros + 10 milhões de certificações
CarOFF - Offline
	Inserção informações do CAR
	Node.js/html5, na máquina local
	Gera um arquivo .car, com um json com as informações textuais e geográficas que o usuário inseriu

Receptor (parte web)
- Onde o usuário envia o arquivo gerado no CarOFF
- verifica sobreposição entre imóveis, com restrições (terra indígena, área de conservação, etc...)
- Há um filtro que analisa e informa se proprietário deve ser notificado

Gestão de acesso - módulo do receptor
- CRUD de usuários
- usuário e senha local, não há integração com login único
- tem demanda para login com dois fatores
- tem captcha: recaptcha

Módulo de análise do cadastro
- gerente operacional visualiza todos os imóveis por uma região de análise
- um imovel tem uma equipe de análise

Regularização ambiental (MRA)
- Se o cadastro estiver ok, sem demandas de retificação da análise realizada, o usuário segue aqui

Análise dinamizada
- Análise automatizada
- Usa o arcgis como ferramenta. Não há regras de negócio, apenas regras de cálculo. "É como uma calculadora". No ArcGis cálculo é executado com Python
- 

Módulo de retificação
- USuário atualiza e gera novo arquivo .car
- depois a análise dinamizada faz o trabalho de verificar se usuário fez o que foi pedido

Central do Proprietário
- 1 milhão e 600 mil
- 20 mil usuários logados em um momento durante o dia
- Visualiza as informações do cadastro realizado no CarOFF e recebido pelo receptor


Fila troca informações com o módulo de análises
- Qual tecnologia de fila? 
	- (O Mateus falou que foi feito em Java, mas disse se tem alguma ferramenta de fila por trás)
- Implementada em java...
- Tem um SqLITE para gerenciar a fila
- Resultado em json

Desafio maior é de infra
- Módulo de consulta pública é o maior gargalo e uso


1.1. Topologia
- 24 máquinas
	- 8 CPU e 16GB d RAM
	- Duas com 64GB de RAM
- Infra é controlada pela Hepta, terceirizada do terceirizado
- Postgree usa replicação. Um banco de escrita e dois de leitura
- Tem mongodb tb - processamentos de relatórios, como se fosse um BI
- 
1.2. Servidores
1.3. Rede


Certificação digital apenas entre o proxy reverso do backend com frontend na DMZ