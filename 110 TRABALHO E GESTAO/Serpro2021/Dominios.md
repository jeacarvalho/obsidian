---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:58.427814+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: modernizacao_cnpj_para_alfa
    weight: 10
    confidence: 0.98
  - name: integracao_redesim_novo_portal
    weight: 8
    confidence: 0.9
  - name: sistema_parcelamento_pgfn
    weight: 7
    confidence: 0.85
  - name: aplicativo_lista_devedores_georreferenciamento
    weight: 9
    confidence: 0.92
  - name: implementacao_waf_siscomex
    weight: 7
    confidence: 0.88
  - name: dimensionamento_ambiente_cdc_cdd
    weight: 6
    confidence: 0.8
  - name: problemas_pucomex_atomikos
    weight: 7
    confidence: 0.87
  - name: migracao_cnpj_oracle_sincronismo
    weight: 9
    confidence: 0.93
  - name: vendas_gov_riscos_seguranca
    weight: 8
    confidence: 0.91
  - name: monitoracao_kafka_ibama
    weight: 6
    confidence: 0.82
  cdu_primary: '351.7'
  cdu_secondary:
  - '347.7'
  - '004.7'
  - '336.2'
  cdu_description: Administração pública. Finanças públicas. Direito administrativo. Sistemas de informação. Gestão de dados.
---
# Descrição: Para tratar assuntos relacionados aos domínios

| links | Arquivos | 
| ----- | -------- |
|       |          |


___
## 20241008 - Apoio time agrobrasil extração informações base CAR via Dataprev
- 

___
## 20240529 - Modernização CNPJ - numérico para alfa
- Até o final de 2025
- Analisar qual a melhor estratégia de mudança da chave primária
- Melhor estratégia por banco?
- Sistemas impactados e rotinas
	- Modele tem um painel para iniciar isso aqui
- Acesso SQLADA 
- Ler git/endevor para identificar quem faz a chamada (NIPJ, CNPJ, etc...)
- Datalake!
	- Carga full?
- estratégia de implantação? O CNPJ é o 1o ou último
- ANDAT vai puxar análise técnica que vai orientar os times nas mudanças
	- Não vamos tocar o projeto
- 

___
## 20231124 - REDESIM novo portal
- https://pnrcidadao-13154.pages.serpro/pnr-cidadao-dasi/topologia.html
- [x] Ver sobre dispensa de RTA para somente banco a ser criado ✅ 2023-12-27
___
## 20230906 - [[SISPAR - Parcelamento PGFN]]
___
## 20230614 - App lista devedores e Lista Devedores
- App usa Sterna como georeferenciamento
- Francisco Wellber Lucena - Lista Devedores
	- Fontes 
		- SIDA
		- Dataprev
		- DW Rio 
			- Pega Dataprev e Caixa com dados de devedores
			- Com isso vai na base da RFB e pega código de município
			- E vão no Sterna pegar latitude e longitude
- Time SUPAI que gera o arquivo georeferenciado - Francisco Timoteo
	  
___
## 20230329 - WAF e Siscomex Carga
- Tem outras questões de infra, com redirecionamentos, tratamento de certificados, tunelamento com Mercosul, que impactam a mudança de colocar um WAF na frente. 

___
## 20230321 - CDC/CDD dimensionamento de ambiente e modelo de licencimento
- 

___
## 20230303 - Problemas Pucomex Recintos com erro no atomikos
- tem erro documentado: https://github.com/atomikos/transactions-essentials/issues/172
- [x] Fechar Siscop 02/2023 📅 2023-03-03 ✅ 2023-03-06

___
## 20230213 - CNPJ e IBM CDC - DR, SUPAI e eu
- Fred - Desenvolve-se na produção
- 

___
## 20230127 - Migração CNPJ Oracle - replicação/sincronismo
- 
___
## 20221021 - PCN VEndas Gov 2a reunião
- Riscos de segurança - se já foi levantado no AMISP para quê outra reunião para isso?
- ![[RiscosAmispVendasGov.png]]
- Sistema de missão crítica? Se sair do ar prejudica população e empresas? Meu Deus do céu! Que é que usa um sistema para comprar e vender imóveis públicos??
- PReciso controlar minha vontade de sempre alocar tempo para fazer o melhor. Talvez cada um dos envolvidos pense da mesma forma, e acredite que essa ação realmente é necessária para um sistema que não vai usar usado por quase ninguém da população brasileira. Tem uma IN que obriga a rever anualmente riscos. Mas por que esse sistema? E se os riscos já estão levantados, por que alguém não cadastra direto no archer? E por que o Dedat precisa estar aqui??
- A vida é curta. É muito ruim perder tempo com aquilo que alguém com alguma autoridade decidiu ser importante. E fez isso sem realmente levar em consideração o contexto maior da vida e da empresa.

___
## 20221013 - Sobre monitoração do Kafka e time IBAMA ser notificado sobre eventos
- Com time da CD que disse que poderia ser feito, mas Jonas discorda.
___
## [[Novo CADIN#202200928 - Novo CADIN X Plin]]
___
## 202200926- Vendas gov
- SPu e [[serpro]] - acordo de cooperação
- inicialmente só fazia exposição de imóveis
- carga de imóveis era um problema
- Tem o Vendas gov multiprodutos, em outro time, códigos apartados
- Mas o que tá no PCN é o vendas gov apenas SPU
- Tem integração prevista com SIAPA Mainframe
- PAI - direito de preferência para quem pagou laudo de avaliação
- Atualizar diagrama
___
## 202200914 - Geral - apresentação sobre evolução do Mainframe
- Ninin apresentando
___
## [[Novo CADIN#202200810 - Apoio Arquitetural - Novo CADIN PGFN + SIRA]]
___
## 20220726 -eprocesso gestão integrada papo Claudinho para entender se pucomex pode ajudar
- Sistemas compartilham banco arquitetura. Java. Asp sendo migrado tb
- Dois app; Internet e intranet
- 2021 surge novo sistema: barramento de serviços
- se api será usada por mais de um sistema, vai para o barramento
___
## 20220726 - Workshop Oracle migração Forms para o APEX, tendo ORDS no meio - Convite PP que está no time do Jones/SUPSE
- ORDS pega PL/SQL e SQL do APEX (monte de procedures e functions no Oracle)
	- Na instalação ORDS tem opção por conversar com outras tecnologias
___
## 20220627 - Vendas gov - time, seat7 e time noSql Sedat (Monteiro, Flavio e Rodrigo)
___
## 20220405 - Pré RTA - RAIA / PGFN
- Diagrama alterar - retirar o que não está no estaleiro, alterar o diagrama informando somente servidor/módulos
	- SIDA não apareceu a integração
- Arquimedes - atualizar
- Módulo batch + online --> Ideal seria estar separado
___
## 20220329 - Nova pré rta Datahub
- [https://cadunicgf-12165.pages.serpro/dasi-ords/](https://cadunicgf-12165.pages.serpro/dasi-ords/)
- Nova necessidade de um processo para posterior atualização das informações das informações dentro do contexto MDM INCRA. 
	- Não está total relacionado ao contexto do RDS
	- Mas dentro do contexto do Incra, será necessário no momento imediantamente posterior ao momento da homologação, time achou que seria interessante aproveitar a estrutura montada do RTA
___
## 20220325 - SPUNET-GCC - Gestão de Contratos de Cessão de Uso - Pré RTA
- Atualizar arquimedes com as integrações
	- Frontend informar angular 12
- Flavors e quantidade de réplicas esperadas no estaleiro?
	- 1 réplica front
	- 1 processador, 2GB RAM
	- Flavor - m4
- Banco de dados: o que é "Modo de criação do Banco de dados: Spring"?
___
## 20220322 - Alinhamento Inicial - Absorção SPUNET-GCC - Gestão de Contratos de Cessão de Uso
- Link do sistema em desenvolvimento: [https://dsv-spunetgcc.df-1.estaleiro.serpro.gov.br](https://dsv-spunetgcc.df-1.estaleiro.serpro.gov.br/)
- Apresentação Bruno Vilela
- Projeto maior de participação de "startups" em projetos do governo
- 5 recursos dedicados ao projeto e +1 recurso de UX
	- Gerente de projeto, 2 analistas de requisitos e 2 desenvolvedores
	- Esse time já desenvolve em ambiente Serpro
- Bruno vai liderar a "startup" criada com esses desenvolvedores
- Futuro: a qualquer momento o Serpro tem que assumir o projeto por ser o provedor de TI do SPU
- Chegou o momento de colocar a solução em produção
	- Absorção parcial para ir aos ambientes de homologação e produção do Serpro
- Tecnologias:
	- Angular (última versão)
	- Spring boot (última versão)
- Autenticação normal no govbr
	- Para perfis chama uma api que vai à base do Acesso gov br
- Hubble + subcontratação
- Desenvolvimento no estaleiro público?
___
## 20211210 - Time DUE e issues Sonar
___
## 20211209 - API CNPJ altíssima disponibilidade
- Api com dependências
- #done Informar ao Galluzzo os contatos para entendimento e uso do gslb
___
## 2021122 - GRSi Inova Simples
___
## 20211117 - SiscoImagem - consulta parametrizada
___
## 20211112 - CNPJ, Elastic, Barramento -  planejamento migração
-[Elasticsearch Search Rejected Queue](https://opster.com/guides/operations/elasticsearch-search-rejected-queue/)
___
## 20211109 - CNPJ, Elastic, Barramento - duas salas, crise e planejamento
___
## 20211108 - CNPJ, Elastic, Barramento
- Migração, talvez por causa da migração do Z15?
- Pensei que era o problema do barramento... Mas não é.
- cluster elastic do barramento estava apontando por um storage compartilhado. Verificou-se que os momentos de lentidão no barramento eram no mesmo momento de storage apitando
- Ponto de controle todos os dias 16h.
___
## 20211103 - Todos, migração z15 (10h - )
- Tudo perdido. Monte de gente não fez o dever de casa. Monte de dúvida.
- E junto com isso migração para teams, sala de crise geral
- [Migração Mainframe - Atualização Z15 - Z15 - Planilhas Google](https://docs.google.com/spreadsheets/d/1aYJ2OrxBIEEuXua-nyTyPgDZvaTahLJ88UcPwtcZGPo/edit#gid=1639443312)
- [Plano de Teste DIDES - Migração Mainframe Z15 - 2021 - Planilhas Google](https://docs.google.com/spreadsheets/d/1hX45ENR6PvT7zqeb4v00CyQCKkLKcqcJRWH4Sy6Z1vk/edit#gid=659168752)
___
## 20211024 - Remessa
- Remessa não chega no estaleiro para conversar com RDOC
- Tinha problema de certificados
- Bernardo
	- RDOC: Estaleiro, xssl client na requisição que informa que exige certificado
	- Remessa tem certificado de máquina e a requisição do remessa precisa informar esse certificado
- RDOC tem um NGINX que precisou ser configurado com o certificado do Remessa, parte pública. 
	- Laubstein sugere retirar esse NGINX porque são 3 pontos de alteração: estaleiro borda, NGINX e backend Java
___
## 20211006 - Processo promoção DRLOA
___
## 20211004 - SUCE - migração estaleiro
___
## 20211004 - Faeserv, cliente, consulta api CNPJ
- Ando, Galluzzo
- Barramentos de vez em quando falham
___
## 20210820 - CNIR (RFb + INCRA) e uso de tecnologias geo
___
## [[Pucomex#20210819 - Pucomex Recintos x nosql SEDAT]]
___
## 20210813 - Inova SPU
- VDI não está no cardápio da subcontratação
___
## 20210810 - Inova SPU - Terceirização SGD
- Aqui o time poderá acessar homologação
- Não é a mesma proposta da subcontratação mas vai se aproveitar bastante coisa lá
- [Protótipo da solução](https://www.figma.com/proto/XXKVipygN1g00lrNFDVTJj/SPU-%2B-Cess%C3%A3o?page-id=8%3A1&node-id=313%3A1534&viewport=53%2C136%2C0.038297273218631744&scaling=min-zoom&starting-point-node-id=313%3A1534)
- Ambiente de desenvolvimento e testes: Rodrigo e Artur vão solicitar acessos com apoio do Deitos
___
## 20210203 - Papo sobre indicador de automação DRLOA
___
## 20210728 - RTA Inova Simples, URC puxando
- Atos cadastrais de uma nova natureza jurídica, empresa simples de inovação - Startup
- Simples Nacional, CPF, CNPJ e TOM, Gov.br - Integrações
- Presentes
	- [[PresentesRTAINovaSImples.png]]
___
## 20210728 - Papo com Daniel Barros (DRCA9) sobre plano desenvolvimento Devops
___
## 20210727 - Time apidue aumento de quota no estaleiro
___
## 20210716 - Apoio drawback comercionalização de api
- Códigos: 36197, 36282, 36131
___
## 20210707 - App Spunet
- Time Daniel Barros, nós e SEAT9
- dúvida era se versiona tudo junto ou não. Vai ter um grupo no git corporativo e projetos separados
___
## 20210706 - Papo com Capacitbr sobre integração com o portal Gov.br
- Em resumo, nas palavras do Flop, a gente não sabe ajudar
- 
___
## 20210701 -Reunião Técnica Dimensionamento / Monitoração / Testes de Carga - Estaleiro - INOVA SIMPLES
- Time da Flavia Andrade: Vando e Fernando Moreira
- 

___
## 20210624 - Barramento CPF
- Alta disponibilidade Data Valid - Em todos os seviços integrados
	- Teriam 3 mudanças:
		- Redundância em outro site da api
		- Mas tb redundância das outras camadas - barramento e elastic
			- Elastic caiu, vai no CPF
		- Falta agora outro barramento BSA
			- Máquinas no ambiente tradicional 
				- 5 wildfly
				- padrão cd (apache na frente)
				- PEdaço data valid, um milhão dia
				- Pedido de duplicar só duas máquinas
	- #done Mandei msg para Jonas e Allston para decidir o que fazer RTA BAR. CPF. Verificar retorno 
		- Marcado para 20210629 17h
	

___
## 20210622 - SINTER/Geo
- Lobinho, Sergio, Rodrigo, JOnas, Clenubio, Bruno
- 

___
## 20210607 - PGFN e necessidade de aumento de quota
- Não tem health check - TEM QUE COLOCAR
- Planilha estava toda errada
- Tudo confuso. 
- PResentes e definição de próximas ações: [[PresentesEAcoesFlexa20210607.png]]
___
## 20210601 - Papo springboot time sispar + sedat
- Marcado internalização juntando times apidue e sispar

___
## 20210601 - Papo apidue com DEDAT, time, SUPCD
- #done Marcar banho de loja com o time apidue

___
## 20210528 - Mudança Acessogov.br no estaleiro
- Cadu entrou para tirar dúvidas do comunicado que foi lançado.
- Entendimento é de que sim, haverá impacto no código.

___
## 20210525 - Apoio time credmei com problema no CEPh/S3. 
- Ao baixar o pdf não está completo
- 

___
## 20210518 - Apoio time SIAPA(SP) no acesso de um serviço no estaleiro
- curl --insecure -H "x-validacao:mobydick" https://siapa.estaleiro.serpro.gov.br/siapa-integracao/api/consulta/indiceacumulado/6/2020
- FUncionou normalmente
>{"indiceBacen":"IPCA-E","indicesAcumulados":\[{"anoReferencia":"2019","indiceAcumulado":"3.913"},{"anoReferencia":"2020","indiceAcumulado":"4.227"}\]}

___
## 20210602 - Suporte estaleiro api-due rdp 66 (Alex e Franklin do time, Eu e Adur, GIsele e Vera Maria Ramos Lotif - CD)
- Gisele apresentando ao time os painéis
- 
___
## 20210514 - Apoio projeto interface PGFN Sonar
- A partir das [Orientações do SONAR](https://devops.gitpages.serpro/aicat/documentacao/sonar/) foi usado um plugin sonar específico no maven

___
## 20210514 - Carga de dados estaleiro time  bConnect (Oggioni)
- Oggioni dando cenário
- Script roda no estaleiro mas envia dados para o blockchain no ambiente tradicional CD
- Orientação: manda o script para a CD rodar, processo "tradicional"
- #done 20210521 - Verificar normativo estaleiro ambiente produção
	- Normativo de uso do estaleiro - [SEGURANÇA DE AMBIENTE DE CONTÊINERES EM NUVEM PRIVADA](https://solucoes.corporativo.serpro/sinor/documento.php?cod=MzY5MjY=)

___
## 20210512 - DRLOA - Recintos
- Comitê para testes do WSO2 produção - Fomos envolvidos
	- SUNIN: Lidiane e Ando
	- SUPSE: Calaça, Bisotto e José Eduardo
	- SUNEF: Lustosa 
	- SUPDR: Samuel Apolonio, Petinari e Sergio Rosemberg
- Vai testar RNF Recintos com WSO2 produção 

___
## 20210511 - Chatbot : DRIEX e SUPAI. SEAT7 ouvinte
- Daniel dando contexto
- Fase atual no driex: prospecção.
### Ronaldo Agra apresentando o tema
- Celina foi um framework inicial para chatbots
- serprobots = Lowcode
	- Flop no wpp - CNPJ treinou bastante no tema
- Bateu no watson, é cobrado do serviço, porque a IBM cobra do Serpro
-  [Site Serprobots - documentação, etc](https://serprobots.estaleiro.serpro.gov.br/)
-  [Canal do chat](https://chat.serpro.gov.br/channel/serprobots-suporte)
-  Foi feito teste com aws chatbot mas o contrato da Ibm era mais vantajoso
-  Vai acontecer turma de workshop agora e outra em julho
-  Há um bot do INCRA em desenvolvimento

___
## 20210506 - Daniel perguntou sobre chatbot
- #done reunião marcada para 11/05 às 10:30 verificar com Jetro sobre chatbot.. Acho que tem algo lá.

___
## 20210505 - MEI x acessogov - DEDAT, Cadu e Igor (equipe Cajado de custos)
- Explicando para Igor a proposta
- decisão de informar todas as premissas, dado o prazo, para que fique claro que é um chute.

___
## 20210504 - MEI x acessogov - DEDAT, URC
- Repassando a solução. Discutindo alterações
- Participação do time do acesso gov para entender o que será demandado deles
	- Falta de sincronia no entendimento de quando existirá o acesso gov privado
- Continuidade: Debate da arquitetura proposta

___
## 20210504 - MEI x acessogov - DEDAT
- Abrir MEI direto dos sites das grandes lojas (MercadoLivre, Amazon, etc...)
- RFB já tinha dito não antes. Mas agora veio por cima.
- Demanda - propor arquitetura de api para que isso seja feito. Robusta, com autenticação, etc...
- Selos na conta do acesso gov.br - ouro, prata, bronze.. .de acordo com a forma de autenticação
- 

___
## 20210430  - Rapello e problema de acesso à módulo no estaleiro
- Era configuração de white list.
- Vai ver qual o ip do procurador e tentar configurar

___
## 20210426 - Papo com Galluzzo e Glória sobre Building Blocks
- Apresentando o que entendemos que é e como vamos ajudar
- Galluzzo
	- Barramento CNPJ - demanda muito grande de utilização (desligamento Tibco, etc..)
	- Até quando a arquitetura atual aguenta.
	- Consulta CNPJ é a mais utilizada
- Glória
	- Dois grandes mundo no barramento: Elastic e Grande porte
	- 

___
## 20210329 - Omissos - cronjob estaleiro
- Jobs parecem não rodar no horário programado
- Problemas na arquitetura da solução. MEsmo com horários corretos de jobs pode haver erros.
- Kohn vai lançar dúvida no canal do estaleiro porque não temos explicação para o que ocorre

___
## 20210329 - [[Pucomex#20210329 - Pucomex migração tibco]]

___
## 20210317 - Erro em produção da PGFN
- Romano pediu ajuda em um RI urgente
>Caused by: javax.net.ssl.SSLProtocolException: handshake alert:  unrecognized_name
Flavio da Silva Nery16:47
https://www-seris.sec.prevnet/seris/SerisWS/SerisService?wsdl
Ricardo Guimaraes Pereira16:51
reCaptcha funcinou com "-Djsse.enableSNIExtension=true"
Caused by: javax.net.ssl.SSLProtocolException: handshake alert:  unrecognized_name
Flavio da Silva Nery16:47
https://www-seris.sec.prevnet/seris/SerisWS/SerisService?wsdl
Ricardo Guimaraes Pereira16:51
reCaptcha funcinou com "-Djsse.enableSNIExtension=true"

- Problema acontece após migrar Java 6 para Java 8.
- [Problema conhecido](https://stackoverflow.com/questions/7615645/ssl-handshake-alert-unrecognized-name-error-since-upgrade-to-java-1-7-0/8769768)
>Java 7 introduced SNI support which is enabled by default. I have found out that certain misconfigured servers send an "Unrecognized Name" warning in the SSL handshake which is ignored by most clients... except for Java. As @Bob Kerns mentioned, the Oracle engineers refuse to "fix" this bug/feature.

- Sugestão: Separar a parte que fala com dataprev para desabilitar: "-Djsse.enableSNIExtension=false". E manter o resto com outro pacote

___
## 20210222 - [[IBAMA Serpro#20210302 - Pedido ajuda Fritz e Gustavo]]
___
## 20210222 - Ruas, Capacidades Críticas e grade
- Ele usa essa [planilha](https://docs.google.com/spreadsheets/d/1tUnwHLvU1iuHMeBxjsJIUKERxLS9OW6KakhOZ9CehdU/edit#gid=754274622) de capacidades. Mesma da nossa
- Fiquei de verificar com todas as redes das capacidades quais serão as questões para que um colaborador seja considerado "capaz":
	- Analytics
	- Big Data
	- IA
	- Mobile
	- Nuvem (AWS)
	- UX
	- Low Code
	- IoT
	- Blockchain
- #done 20210301/20210322 - Ver questões para capacidade crítica - Ruas
- #done 20210329 capacidade crítica - verificar o retorno do Dedat sobre questionários - Jonas enviou email em 04/2021 

___
## 20210212 - [[IBAMA força tarefa estaleiro - notas do chat]]

___
## 20210205 - [[e-Sapli#20210205 - 1a Reunião Arquitetura Gerenciador]]

___
## 20210203 - [[MEI#Equipe MEI 20210203]]

___
## 20210201 - [[MEI#Cadu 20210201]]

___
## 20210119 - [[DWBK Isenção]]

___
## 20210118 - CNPJ

- Ver sobre TIBCO para Débora (email de 20210118) 
	- Respondido em 20210127