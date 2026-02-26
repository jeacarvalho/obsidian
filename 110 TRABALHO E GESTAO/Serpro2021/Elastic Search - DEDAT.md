### Descrição:

| links                                                                                        | Arquivos |
| -------------------------------------------------------------------------------------------- | -------- |
| [Documentação elastic time NoSql](https://git.[[serpro]]/dedat/nosql/elasticsearch/documentacao) |          |


___
## 20250306 - Reunião semanal do ANDAT - Thiago Monteiro explicando a nova contratação de elastic que será realizada
- tem um gitlab para solicitações de subscrições. Pedidos serão formalizados por uma issue lá
- cada equipe local deverá avaliar os pedidos
	- Material para ajudar nisso? Questionários, etc?
- 


## Reuniões entre 20210315 e 20210810
___
####  20210810 - Informei ao sedat-nosql que ambiente de monitoração do Recintos foi criado
- [Issue de acompanhamento do suporte Elastic ao Pucomex Recintos](https://git.serpro/dedat/nosql/planejamento/-/issues/35#note_837078)
- #done Verificar com time recintos o acesso ao cluster RNF do elastic

___
####  20210525 - JOnas encaminhou planilha para preenchimento dos times
- [Planilha Elastic clusters Serpro 202105](https://docs.google.com/spreadsheets/d/18O7S7LFcAU5AvKSLg62TuF7zQ2ho67TvYfh9d5EhLys/edit#gid=0)
	- #done 20210527/26 Preencher com CNPJ os campos da planilha elastic
		- Mandei email para Jovando em 20210526
___
####  20210524 - Thiago encaminhou documento
- [monitoração do cluster elastic, o caminho](https://git.serpro/dedat/nosql/elasticsearch/documentacao/-/blob/master/README.md#7-monitora%C3%A7%C3%A3o-do-ambiente)
- [[PROJETO LÓGICO DE BANCOS DE DADOS NOSQL.pdf]]

####  20210519 - Apresentação Asper sobre recursos da possível contratação
- 

####  20210517 - SEAT7 + Time Elastic - Caso Recintos
- Problemas:
	- Mesmo cluster para consulta a inserção
	- Mesmo cluster para todo Pucomex
	- O que já pode mostrar que elastic como base única não parece ser mais adequado (Monteiro)
- Monteiro: Se não usa full text search iria para o mongodb
- Modelagem: o time ajuda, mas não na reunião de segunda. Marcar outra agenda e negociar tempo com lideranças
- [Documento do Monteiro analisando a questão](https://git.serpro/dedat/nosql/elasticsearch/documentacao/-/blob/master/README.md#armazenamento-de-documentos-como-base-persistente-elastic-como-base-de-dados-de-neg%C3%B3cio-)
- Vamos entrar no canal do chat do time elastic para colocar outras dúvidas que restaram

####  20210512 - Apresentação Asper dos modelos de subscrição
- [[NiveisSubscricaoElastic.png]]
- Gold - "níveis de consultoria". Quem define?
- Subscrição paga para nodes (gold, platinum) e "unidade de recurso enterprise" (Enterprise)
	- Nodes em qualquer configuração de máquina (ou seja não muda se for mais parruda a máquina)
	- No mundo "enterprise"  os projetos devem ser migradas para um novo formato de servidores para o elastic com padrão "conteiner"
	- Se termina o contrato?
		- Pode continuar usando o ECE, desde que não tenha nenhuma ação. Reiniciar, nova instalação, ECE não permite. Assim, tem que voltar para nodes
- Unidade de recurso enterprise - a cada 64gb de memória em uso

####  20210322 - DEDAT, Asper, Lobinho
- Jonas colocando dúvidas que surgiram no trabalho
	- Consultoria é uma possibilidade como modelo de contratação?
	- Asper: órgãos que tiveram sucesso: subscrição e serviços de apoio
		- Nunca viu um processo de contratação só com serviços, sem subscrição
	- Asper, Marina: Dataprev tb está em fase de contratação
		- Ata de registro fechada com bolsão de horas de apoio
		- Bolsão de subscrições, priorizável conforme o projeto
- Jonas: Cluster instalado, supondo que faremos subscrição
	- Temos que migrar o cluster para versão ECE ou podemos aplicar na instalação que já temos?
	- Asper, Pedro: **Enterprise** via conteiner Docker. Nesse caso teria que migrar o ambiente com cluster ECE. Migração não seria custosa 
	>Jonas entende (na [[Reuniões SEDAT#20210323 - Gerencial DEDAT]]) que a volta tb seria possível pelas palavras do fornecedor.
	- **Platinum** poderia aplicar no nó já instalado e com a versão atual
	- **Gold** tb poderia ser como platinum, mas tem recursos muito inferiores. Seria uma versão inicial das subscrições. Suporte horário comercial. Nas outras, 24 X 7
- JOnas: Uso do elastic com SIEM
	- Asper (Fabrício): Sim, ocorreram POCs sobre isso. COnversar com as equipes de segurança
		- Curi em [[Reuniões SEDAT#20210323 - Gerencial DEDAT]]: Iahn não conhece sobre essas pocs
- Como uso de cache
	- Asper (Pedro): não houve o uso de cross site (replicação) mas é algo simples e muito utilizado segudo eles.
- Jonas  - Kibana tem aspectos de auditoria que podem ser habilitados?
	- Asper (Pedro): 100% nativo, é só habilitar o recurso
- Asper (Fabricio): qualquer dúvida, podem marcar um papo de 10/15 minutos para explicar tecnicamente alguma coisa.
	- Contato Fabricio: (61) 981223301

####  20210319 - Elastic CNPJ - entendimento Poc
- Marcio Costa e Carlos Glória 
- SP, SVD, RJ, CTA (SEDAT)
- Jean Leite e Douglas Oyama
	- Participaram desde o início do elastic no CNPJ
- Marcio: Ainda não temos um suporte bom no elastic
	- Batemos muito cabeça
	- Mas na visão dele mais organização seria mais produtivo
	- CD sempre disse que queria estudar e não consultoria
- Glória: Luis Adriano participou ativamente da poc e teve muito contato com a consultoria
	- elastic versão 7 (não lembra o minor)
	- Atual já é mais à frente
	- objetivo poc: descobrir qual a capacidade de nosso ambiente
	- replicou a produção e adaptou com as orientações da consultoria
	- Teste de estresse: 
		- jmeter ativado em fortaleza
		- 2100 req/s chegando ao barramento com nível de serviço aceitável sem que a estrutura de ativação + jboss + rede caísse
			- Nesse momento o consultor disse que elastic ainda estava tranquilo
	- 5 máquina com jboss estrutura que acessa o elastic
		- 10 nós no cluster
- Márcio:
	- Foram várias pocs desde o início do elastic no CNPJ
	- sempre tivemos dificuldade em saber montar o ambiente correto
	- produção hoje com 8 máquinas elastic
	- não tem painel de monitoramento de todo ambiente
	- Consultoria ajuda muito.
	- Ou subscrição ou treinamento deequipe interna
- Glória:
	- Distribuição de shards por índice - feito com o pessoal do elastic na consultoria
	- não evoluiu a aplicação para a forma mais moderna de uso do elastic
	- Ao consultor: "As querys estão ok?" - Consultor: "Sim."
	- keep alive na frente faz distribuição aos nós elastic
- Peter:
	- Elastic é cache? 
		- Glória: Começou com consulta pública mas virou um barramento para as consultas ao CNPJ
		- Marcio: No barramento - direto por chave
			- Monteiro: chave é ID do índice ou campo indexado por chave
			- Marcio: CNPJ é ID. Há uso de full text mas é pequeno
	- POC foi melhor?
		- Marcio: sim, mas era outro ambiente, outras máquinas, discos melhores, além da própria versão 7 e a configuração pela consultoria
		- Carlos: Sim, a **questão da configuração foi o diferencial**, especialmente na configuração de discos
			- Maioria dos problemas até aqui no uso do elastic foi de disco
			- Outros problemas não foram ligados ao elastic. Keep alive por exemplo.
- Monteiro: monitoração, como estão lidando?
	- Marcio: monitoramento interno do serpro não entende o elastic
		- Somos fracos (minha leitura)
		- Não temos o monitoramento no cluster
	- Glória: no desenvolvimento não temos visão do elastic. A não ser um grafana da CD para ver memória cpu e disco no nível máquina
		- Elastic tem uma solução de monitoramento muito interessante (isso já foi citado antes...)
		- Desenvolvimento instrumenta os logs para tentar monitorar via eles com um kibana lendo
		- Nem tudo de monitoramento está disponível no gratuito mas o que se tem nessa versão já poderia ajudar muito.
- Eu: A ferramenta livre atende ou temos coisas pagas que poderiam ser importantes?
	- Na visão do Carlos, igual ao do Márcio, treinamento e organização seriam mais importantes


####  20210318 - Elastic Nfe - entendimento Poc
- Cache do Sql Server
- Leandro de Paula dando um contexto: A ferramenta livre atende ou temos coisas pagas que poderiam ser importantes
- Jonas: demanda - organizar uma possível contratação do elastic
- Celio Nogueira apresentando o histórico do uso do elastic na Nfe
- Desempenho foi bem complicado de fazer
- Versão basic atendeu a tudoo que era necessário na POC inicial de uso na Nfe
	- 17 questões de negócio - funcionou tudo sem nada de entreprise
- Enterprise: facilidade de alocação, gerenciamento
	- Licença dá outras capacidades: machine learning, relatórios, acesso a repositórios ldap
- Complicador: a licença nova do elastic
	- objetivo: conter [avanço da aws](https://www.elastic.co/pt/blog/license-change-clarification) no uso do elastic.
	- mas a licença demanda que todo software que usa o software deve ser livre.
- Jonas: 
	- discussão da licença já ocorreu. Quem usa sem customizar não precisa ser open source
	- tunning, etc, na poc, foi feita pelo fornecedor


####  20210318 - DEDAT
- Jonas usando [esse documento](https://docs.google.com/document/d/1gvi9h0p7tDn9mmhkrEhQxN7aFhS0TNik6yMcI9p_bTQ/edit) para repassar com todo dedat
- Thiago Monteiro e Peter comentaram sobre a importância da consultoria e até do treinamento/desenvolvimento dos times na tecnologia


####  20210315 - Gerencial DEDAT
- Elastic
	- [Material compartilhado](https://drive.google.com/drive/folders/16A7PZhdPyb9aci5P1bNyRn8a0gxbZ7cg) com os times que vão trabalhar no assunto
	- demanda: fornecedor fez pocs. Para ele justifica-se a necessidade da subscrição. Mas nem CD nem DIDES tem essa visão. DEDAT vai arbitrar se é necessário ou não, justificando qual o cenário se aplica.