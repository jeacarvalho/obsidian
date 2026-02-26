# Descrição:

| links                                                                                                                                                                                                                                                 | Arquivos                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| [Proposta para uma nova estratégia para o controle florestal brasileiro e o combate ao desmatamento - IBAMA](https://brasil.mongabay.com/2021/07/proposta-para-uma-nova-estrategia-para-o-controle-florestal-brasileiro-e-o-combate-ao-desmatamento/) | Arquitetura geral [[MMA-TD.png]]               |
| [Formalização de Oportunidade de Negócio - RFP / MMA](https://docs.google.com/document/d/1CwdSskFupAmVcVmwRlclY8UDNFk2HKyzDRBi5zW1udw/edit)                                                                                                           | Arquitetura app [[MMA-TD-APP.png]]             |
|                                                                                                                                                                                                                                                       | arquitetura Laudos [[MMA-TD-Laudos e DNA.png]] |

___
## 20220805 - Arquitetura geo analítica
- 

___
## 20220726 - Apresentação do DETEX pelo Ibama

___
## [[Custos SUPSE#20220719 - Custos da arquitetura mais madeira]]

___
## 20220712 - Hjort apresentando planilha que montou para responder o quanto a arquitetura proposta atende requisitos do projeto
- 68% atendido. Restante sobre processamento de imagem
- 


___
## 20220706 - Apresentação arquitetura URC
- #done Procurar Igor/Cajado para precificarmos a proposta de arquitetura para o mais madeira

___
## 20220607 - Retorno sobre dúvidas e respostas da parceira
- Parceira reafirmou que vai, sim, desenvolver. Aumentou quantidade de horas na proposta. Processo vai prosseguir
- Volta necessidade de termos evolução de arquitetura que precisamos para contemplar o projeto como um todo.
- A ideia é chamar já a Stefanini agora para ajudar na definição da arquitura da solução
- Dúvidas que levantamos:
	- Adaptações sistema não farão parte da estimativa do ambiente mais madeira
	- Processamento de imagens será realizada na infra do [[serpro]] ou por infra provida pelo Serpro. 
	- Processamento de imagens - não reinventar a roda. Ter algum tipo de parceira com INpe ou Serviço Florestal para reutilizar algoritmos deles.
	- "O inventário nacional, RADAM Brasil, SISPROF elencados na segunda etapa da figura, bem como o Flora Brasil, inventários florestais estaduais – apresentados no diagrama “Solução Analítica” na página 15 do documento, são dados raster, polígonos ou dados tabulares “normais”?" - Não se tem certeza mas termos um pouco de tudo...Não tem volumteria nesse momento.
		- 150 MB cada banda de imagem - Hjort
	- "A “malha para avaliação de coeficientes de transformação”, citada na etapa 4, após a criação do DOF de transporte ao primeiro desdobro é algo existente no DOF rastreabilidade ou uma funcionalidade a ser criada no escopo do Floresta+ madeira? " Não é geo na visão do Hjort
		- URC acha que já tem cadastro no Sinaflor+ mas o app não cadastra nada
	- "Qual o tipo de cruzamento de dados previsto com a NF-e? Há alguma volumetria prevista para esse acesso aos dados daquele sistema? "
		- Fred vai conversar com sistema de origem do DOF para entende ro modelo (1x1?) para termos volumetria
	- "Na imagem da página 11 do documento é citado um “DWR”. Trata-se de um datawarehouse? Se sim, quais integrações estão previstas? Não encontramos nenhuma outra informação no documento. Da mesma forma quanto aos sistemas já em produção do Serpro, a equipe que mantém esse DW deve ser contactada para verificar se há impactos previstos naquele sistema. "
		- Banco grande que eles tem um Oracle que agrega tudo. Vai ser confirmado com o Ibama
	- "App vai gerar informação e precisamos prever infra para isso"

___
## 20220510 -
### Itens a terem insumos
#### Já existentes
- SInaflor, DOF, Sinaflor+ e integrações
	- SINAFLOR p. Integração com CTF, ADAWeb, CAR
- Sinaflor+ - Declaração de corte já existe?
- DOF tem todas as informações necessárias á etapa 4?

#### Para Alertas
- Obtenção de imagens de satélite - módulos de atualização? Vou ler de fora os atualizados? 
- Cadastro de regras e parâmetros para processamento das imagens. Quais biomassas são permitadas? Quais fitofiosnomias são permitidas
- Cadastro de padrões de dados?


### Dúvidas
- Doc p 8 imagens de satélite para cruzamento se há floresta - onde obter? Automatizada? Se sim, tem um módulo
	- Balanço florestal (áreas sob regime de exploração - no novo sistema ou em algum lugar?
	- Balanço florestal (áreas sob regime de exploração onde será o cadstro desses dados?
	- Autorizações emitidas em determinada delimitação geográfica  SINAFLOR?
	- Avaliação de performance - no mais madeira?
- 3a etapa p. 9 no Sinaflor+ - A desenvolver?
- 4a e 5a etapa DOF - alterar?
- Rotas existentes no DOF

### Grandes etapas - figura p.11
[[FluxoMaisMadeira.png]]
#### Etapa 1
- Insumo SINAFLOR projeto exploração
- Insumo geo: Imagens orbitais mapea. fisionomias e biomassa
- Output: alerta existência de floresta

#### Etapa 2
- Insumo etapa anterior
- Insumo geo inventário naciona, RADAM Brasil, SISPROF, etc
- Output: alterta busca padrão de dados (qual?)

#### Etapa 3
- O que são AUTEX, ASV, UAS?
- Insumo Sinaflor+: declaração de corte
- Insumo geo: Imagens orbitais (mesma imagem e fonte do alerta 1?), mistura espectral detex, NDFI
- Output: alerta de sinais de exploração implantação de estrutura na floresta
- autorização de supressão de vegetação (ASV), Autorização para Exploração Florestal (AUTEX), uso alternativo do solo (UAS)

#### Etapa 4
- Insumo DOF - DOF de transporte ao 1o transbordo
- Insumos (mais madeira? ou onde?): Grau eficiência tecnologia, análise de CRV ou MDC, Analise intervalo de confiança
- Onde estão os parâmetros de malha? é no DOF?

#### Etapa 5
- INsumo DOF - DOF de transporte para comércio e exportação
- Insumos (mais madeira? ou onde?): Análise de tendências, análise rotas (cadastradas no APp ou em outro sistema, cruzamento NFE - qual?

### Seguindo
- p. 12 "acoplados a modelos parametrizados por agentes públicos" - onde foram parametrizados? Serão parametrizados no mais madeira?
- DWR - Data warehouse?
- p. 13 - quais sistemas serão construídos ou adaptados? Estão no Serpro os adapatáveis? O aumento de funcionalidade impacta aumento de ambiente produtivo?
- **7 (sete) módulos** p. 14 que agregam e apresentam visões analíticas para  
as etapas da cadeia produtiva, permitindo visões Estratégicas (nível gerencial) e Tático  
Operacional + **serviço de entrega de dados aos órgãos de controle**.  
- Módulo de Empreendimento e Projetos
- Módulo de Inventário Florestal  
- Módulo Performance dos Responsáveis Técnicos  
- Módulo Exploração  
- Módulo Industrialização  
- Módulo Transação  
- Módulo Exportação
- p. 11 cita "módulo monitoramenteo de variáveis"

### Automação de polígonos já existe no time do Hjort
- Tiago Flores tem conhecimento

### Painéis - 5, um para cada etapa
- Item 15. p. 27 --> Cruzamento dos limites da área a ser explorada com imagens de satélite
- Item 16. p. 29 --> Cicatrizes de exploração
- Item 17. p. 30 --> Grau de eficiência tecnológica da cadeia produtiva
- Item 18. p. 31 --> Volume de determinada espécie transacionado
- Item 19. p. 32 --> Informações vetoriais da área sob regime de exploração e pontos de  
coordenadas

___
## 20220509 - Com SEAT7 entendendo o documento - [[RFP - IBAMA - Resumo.pdf]]
- Obtenção das imagens - não somente satélites, mas tb google (que junta fotografias aéreas com imagens de satélite)
- delimitação de áreas - cadastra no mais madeira ou já vem de outros sistemas que fazem esse cadastro (sinaflor)
	- Cadurb seria isso?
	- Onde seria feito esse pedido de desmatamento?
- Controle da madeira - 
- 5 etapas
	- Sinaflor - juntar bases
	- Inventário florestal - limites de áreas exploradas, etc
	- Declaração de corte da árvores - espécie, pode cortar, áreas que tem mais espécies
	- Utilização de recursos florestais - acompanhamento da madeira - do corte à 1a empresa a beneficiar
	- Acompanhamento ao usuário final - caminhão, rota, destino.. Esse destino é coerente? o tipo de madeira é usado realmente nesse destino


___
## 20220506 - Reunião do projeto com time externo
- [Projeto Floresta+ Madeira | Microsoft Teams](https://teams.microsoft.com/_#/conversations/19:meeting_MWVlNTZjNzktM2ZkMC00MWRhLWI4YmItYTkwMmQ4YzNjMTNj@thread.v2?ctx=chat)
- Há impacto previsto nos transacionais do IBAMA para o Floresta + Brasil
- Durante toda reunião pareceu soar um tema: O serpro não tem conhecimento então precisamos arrumar jeito de arrumar dinheiro para que tenha uma consultoria junto.
	- Mas se o Serpro tivesse gente e conhecimento o IBAMA teria dinheiro para bancar?
- Rafael Freire de Macedo - coordenador do projeto no IBAMA
	- Entende que o projeto é complexo e grande
	- Outros projetos devem vir para essa estratégia de financiamento externo com Serpro sendo o contratado, com suas parceiras
	- Plataforma Bem-te-vi + 1
	- Copérnicus - satélite Sentinel faz parte desse projeto da União Européia
- Edilaine (URC)
	- Dando histórico
- Adriano Ávila (SGTI do IBAMA?)
	- Subcontratação não está bem azeitado na esplanada
- Fred
	- O que mais preocupa é detecção de padrão em cima de imagens
	- Discovery, detalhamento requisitos, precisa da participação do IBAMA com o conhecimento e as necessidades, mesmo na relação com a parceira
- Liliane Pereira dos Santos - Coordenadora de outra área no IBAMA
	- Vendendo o peixe para receber concursados novos do IBAMA para a TI acompanhar o projeto
- João Pessoa Riograndense Moreira Junior - Diretor
- Raquel Sabaini
	- Aproveitando a reunião para apresentar necessidades ao Serpro e tentar entrar nessa esteira de transformação digital/percerias
	- SIMAFI é o sistema. Fazer um app e colocar georeferenciamento. Já está sendo sustentado no Serpro
- Daniel Santos PInho
	- Mesmo caminho da Sabaini, sistema de rastreabilidade Pirarucu
	- Tem até agosto para contratar
- Rodrigo Hjort - dúvidas técnicas
	- Sistemas do INPE - Fizemos trabalhos de cruzamento geoespacial com algumas bases de lá

___
## 20220503 - [[IBAMA Serpro#20220503 - Arquitetura Geo Analítica]]
___
## 20210913 - Reunião inicial com Tiago
- App para caminhoneiro, com integração NFE e Denatran
- 

___
## 20210908 - Reunião inicial com Jonas
### Plataforma mais madeira
- [Proposta para uma nova estratégia para o controle florestal brasileiro e o combate ao desmatamento - IBAMA](https://brasil.mongabay.com/2021/07/proposta-para-uma-nova-estrategia-para-o-controle-florestal-brasileiro-e-o-combate-ao-desmatamento/)
- Parceria de transformação digital - Serpro escrevendo uma RFP
- [Formalização de Oportunidade de Negócio - RFP / MMA](https://docs.google.com/document/d/1CwdSskFupAmVcVmwRlclY8UDNFk2HKyzDRBi5zW1udw/edit)
- Tem time de analitycs, Machine Learning, IA, GEO
- Mas a parceira não vai obrigatoriamente desenvolver. Pode ser só estudar e informar a melhor solução
- Jonas entende que Flop poderia fazer aquela apresentação que fez para o SEDAT do building block geo
- Avaliar se o projeto está ok, e se seu desenvolvimento faz sentido (saiu a madeira? Tem estrada?). Além disso, pode avaliar trabalho dos engenheiros florestais que acompanham e aprovam projetos