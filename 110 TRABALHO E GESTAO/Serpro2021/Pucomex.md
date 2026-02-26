___
## 20220710 - CCT Exp melhora de código
- Ver com Paranhos e MOtta alocação do Caçador e Vítor
- Atualizar scripts de RNF para execução e entendimento de onde estão os gargalos atuais
- Propor mudança do requisito de negócio para processamento assíncrono
- Anotar código com métricas usando o que o Plataforma já disponibiliza - Adur
- [x] Ver no SEDAT quem toca APM para ajudar o CCT Exp na melhoria do código 📅 2023-07-15 ✅ 2023-07-18
___
## 20220324 - RTA Anexação e RTA Loja franca
### Loja franca
___
## 2021130 - GT Arquitetura e IBM MQ
___
## 2021104 - Problema elastic CNPJ impactando Pucomex
- Houve instabilidade no barramento cnpj, identificado no elastic, pelo que entendi
- Houve um aumento de threads no apache de entrada, dobrando o número para 4k. 
- Normalizou, mas o horário também pode ter sido o motivo
- Thiago Monteiro participou. Monitoração apresentada pelo time elastic CNPJ não pareceu mostrar o que ele solicitou. 
___
## 2021103 - Reunião gt arquitetura com time técnico IBM MQ
- TIme técnico era desnecessário aqui.
- Primeiro deveriam ter mandado orientações sobre contrato, consumo de horas, forma de alocar, solicitar. Depois, com time técnico da IBM, faríamos a reunião£
___
## 20211028 - GT Arquitetura migração IBM MQ
- "Redelivery Delay" - ainda aguardando resposta do LAB IBM
- 

___
## 20210821 - Pucomex e IBM MQ (Rene)
- Bridge x Tópicos
- [Pucomex migração tibco](https://pucomex.gitpages.[[serpro]]/documentos/arquitetura/migracao-tibco/#tibco)

___
## 20210819 - Pucomex Recintos x nosql SEDAT
- Papo com Thiago Monteiro para um suporte e orientação sobre otimização de consultas

___
## 20210705 - Pucomex DUEX com problemas de muito acesso ao banco devido ao consumo da fila
- 

___
## 20210628 - Criar plano de evolução DevOps da DIDES
- Papo com DRLOA, Jonas e eu
- cheguei tarde porque estava em [[Geo#20210628 - Reunião Imagem Esri - Visões de gerenciamento territorial e dados geográficos em órgãos federais]]
- 

___
## 20210621 - Papo alocação SEAT7 no CCT
- Jonas, Paranhos, Motta e Eu
- 50/50

___
## 20210611 - Pucomex CCT IMP
- Analisando procfile e verificando otimizações e correções na configuração
- Propondo os ajustes e testes
- Informando que JAXB pode ser um problema com metaspace

___
## 20210607 - Elastic recintos
- Jean Leite presente. Ele está vendo esse movimento do elastic se tornar a base única dos sistemas. Mas é a maior preocupação dele no momento do Serpro
	- Há dois ou três projetos que o Elastic já é a base final: Sigep autoriza
	- Cd serviço 11682. Não encontrei módulo no arquimedes com o elastic. Mandei email para o gestor técnico informado no meu domínio (guilherme.soares-carvalho@serpro.gov.br)

___
## 20210527 - Pucomex - subcontratação
- Debate sobre os riscos
- Participação de Cláudio e Ruas no final
- [Documento de riscos do Pucomex](https://docs.google.com/document/d/1NlUUrLJJV2Dgy21lJv7fqPhVwn3hg49G3pjGiECLHXg/edit?usp=sharing)

___
## 20210519 - Elastic Recintos
- Adur repassou o que iremos conversar mais tarde com o time
- Adur apresetando ao time mais URC

___
## 20210426 - Continuidade Elastic com SEDAT (SPO e CTA)
- Adur dando cenário
- [Arquitetura Elastic Pucomex](https://pucomex.gitpages.serpro/documentos/configuracao/gcs-elasticsearch/)
- Monteiro, cenário: 
	- Equipe de suporte, Bruno Assunes, recebendo agora esse repasse - 42 clusters de elastic na CD
	- Conhecimento é muito restrito (poucas pessoas) e menos polido do que Oracle e PostgreSQL


___
## 20210426 - Recintos / Elastic 
- JP explicando a necessidade
	- Recintos precisar ser realmente 24/7
	- Tiago Barbosa questionou duas bases. 
- Time apresentando diagrama de fluxo
- PElo entendido:
	- Começou com ORacle por ser receita (Sief)
	- Elastic surgiu com necessidade de consultas de outros sistemas
	- "Regra de RFB" para uso do Sief pode ser flexibilizada pela SECEX
	- O sistema poderia ficar somente no elastic, porque a transação com Oracle só se mantém como fallback
	- Questões:
		- Suporte na CD - É preparado para manter um sistema de 1000000 de registros diários só no Elastic? 
		- Arquitetura vê algum risco para uso somente da base elastic?
- Sistemas utilizando mongodb: [Indicador de Automação - Grafana (serpro.gov.br)](https://painelgovtec.serpro.gov.br/d/cu1RyZeWz/indicador-de-automacao?orgId=1&var-sistema_filter=All&var-modulo_filter=All&var-estaleiro_filter=All&var-plataforma_filter=All&var-tecnologias_filter=mongo)
- #TD - COnsular SEDAT e SUPCD sobre uso do elastic com banco único

## 20210415 - Reunião GT REQ Problema do ACD na DUE 
- [quadro do miro com diagrama inicial](https://miro.com/app/board/o9J_lSe0AEw=/)


## 20210414 - Reunião geral Problema do ACD na DUE 
- Problema do ACD na DUE - vez ou outra CCT e DUE perdem em sincronismo
- Suspeita: release eufrates, reduziu visões e aumentou servidores nas visões que ficaram
- Assunto subiu. Sala de crise? Vai pegar mal se erro for em código
- Dois caras cavando e 13 olhando
- JP: Monitoração de DUEs  que estão esperando por muito tempo
	- CADU: Solução Moura no Mantra. Apes de noite para mostrar dues com problemas
- Vai ser montado um grupo inter sistemas para trabalhar.
	- Por enquanto não vamos ter dedicação exclusiva. 

## 20210406 - Naiana, Petinari, Adur e Eu - Logs do Recintos
- Cenário
- [documentação do estaleiro sobre o default do graylog](https://docs.estaleiro.serpro.gov.br/ofertas/servicos/laas/)
- Solução?
	- Volume persistente para direcionar o log para lá. RNF Adur já tinha feito
	- Executar o fluxo em um ambiente para ver o que tem de log para definir o que vai manter
	- Alterar o código retirando ou aumentando o nível de log onde for necessário mudar (inclusive com configuração de log por pacote no caso do componente de fila)
	


## 20210405 - Email Jonas sobre log do Recintos
- Agendada reunião para 06/04

## 20210329 - Pucomex, migração tibco

-   Apresentação do GT arquitetura para o time de gestão e desenvolvedores
-  #done - Não consegui resposta 20210506 - Sustentação CD do WSMQ - Verificar com Rene/Bisoto porque se levantou que a CD não tem experiência suficiente para dar suporte ao uso. Comentado com Bisotto. Aguardando
		-  Enviei msg no chat no mesmo dia (29/03), sem resposta até 05/04
		-  Enviei email em 05/04
		-  Envie msg wpp em 08/04