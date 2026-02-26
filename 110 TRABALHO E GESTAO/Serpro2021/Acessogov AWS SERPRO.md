# Descrição:
- Para acompanhar e documentar ações, reuniões, etc, do trabalho do sedat na migração do acessogov para aws

| links                                                                                                                                                       | Arquivos                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| [projeto no git para acompanhar](https://git.serpro/dedat/acessogovaws)                                                                                     | [[DAS_img_Arquitetura_BrGov_NoIP.pdf]] |
| [Kanban projeto "maior"](https://kanban.serpro.gov.br/?controller=BoardViewController&action=show&plugin=&project_id=4382&search=category%3A%22Sprint+3%22) |                                        |
| [Pad do Bastos CI/CD](https://pad.serpro.gov.br/p/acessogov-gitlabci)                                                                                       |                                        |
| [Faq com problemas da migração do staging](https://dedat.gitpages.serpro/deatf/migracao-acesso/)                                                            |                                        |

___
## 20220512 - Revisão Sprint 15 e definição de data para migração
- 

___
## 20220329 - Revisão sprint 12
- 

___
## 20220302 - O que vai e não vai do acesso para nuvem
- A pedido do Wilton
- 
___
## 20220224 - SUPAI e serviço elastic
- Hanns, Machado, Amaral, Hugo  e Jonas
- Fred ger. departamento, Saint clair substituindo. .Jonas envolveu ele.
- Funcionalidade: ingestão de log de auditoria do postgre para elastic
- São duas funcionalidades à migrar: a que faz atualização e uma api que consulta o elastic
- Decisão: time SUPAI vai migrar com nosso suporte (SUPSE/SEDAT)
- #done Confirmar versão do Elastic na aws para ver se tem diferença

___
## 20220223 - Migração LDAP para postgre na aws
- Foi fechada a estratégia de ter dois programas. Um com carga full para iniciar e outro que atualize somente o diff

___
## 20220221 - Papo sobre criação de DNS secundário que poderia trazer impacto aos desenvolvedores que se integram ao acesso via vpn e a clientes que acessem via intranet
- 

___
## 20220215 - Revisão Sprint 10 e planejamento Sprint 11

___
## 20220202 - Planejamento Sprint 9

___
## 20220201- Revisão Sprint 8
- 

___
## 2021222 - Planejamento Sprint 6

___
## 2021221 - Retrospectiva Sprint 5
- 

___
## 2021207 - Retrospectiva Sprint 4

___
## 20211123 - Planejamento Sprint 4

___
## 20211123 - Retrospectiva Sprint 3 projeto maior
- bla bla bla
- To querendo, muito, saber como dar utilidade e valor a isso aqui

___
## 20211110 - Planejamento Sprint 3 projeto maior
- bla,bla,bla
- três reuniões de blablabla

___
## 20211109 - Revisão Sprint 2 projeto maior
- bla,bla,bla


## 20211027 - Planejamento Sprint 2 projeto maior
- Muita conversa, mas muita falta de objetividade e direção. 

## 20211025 - [[Relatório Adur staging período minha licença]]

## 20211001 - Ponto controle
- [Ferramenta para validar scripts terraform](https://github.com/bridgecrewio/checkov)

## 20210929 - Retomada do projeto de migração após POC RHSSO - AWS e [[serpro]]
### Parte I - manhã
- [[ParticipantesReuniaoAcessoAWSSERPRO20210929.png]]
- Fernanda dando introdução
- Necessário prazo de projeto para obtenção de custos
- Orlando/AWS conduzindo

### Parte II - Tarde
- 

## 20210929 - Posicionamento Jonas
- Deitos veio de outra reunião anterior sobre o projeto e com a decisão de seguirmos como estamos
- Embarque seguro
	- 

___
## 20210923 - Reunião time
- Segundo dia sem participação do Cleiton
- Reinaldo não participou
- E não conseguiu falar com Cleiton sobre versão de estado atualizado no git, segundo Bastos
- Flavio, no chat:
>Flavio Gomes da Silva Lisboa 16:03
>Reinaldo postou no chat "Não vou conseguir participar do ponto de controle com a DIDES agora. Quem for participar avise que ainda estamos com problemas de conectividade com o banco de de dados da AWS para o Serpro. Obrigado!"
- Sugeri, no seat7 apenas, que a gente empurrasse trabalho para os outros caras da CD. Entendimento de Flop e Adur é que trabalho é empurrado e eles deveriam puxar. Meu entendimento é que vão dizer depois que não demos trabalho para eles.

___
## 20210920 - Reunião time
- Distribuindo issues milestone M1 e apresentando planejamento M2

___
## 20210917 - Reunião time
- DNS - será no Serpro, conforme Reinaldo disse na reunião. Algo já decidido anteriormente em reunião com o pessoal da rede
- Vamos usar o route 53 para dns temporário até o final do trabalho de infra básico
- Reinaldo - testou solução do Marcelo pra pipeline
	- plan do terraform pede credencial. Qual será no caso de pipelines?
		- iAm user ou credencial pessoal?

___
## 20210913 - Reunião time
- [Documento de dúvidas do time para apoio da AWS](https://docs.google.com/document/d/1CO40Nd0ZVyK0pX8eKs3xmXvze1cQ_ONpa4EmxFBWhDQ/edit)	

___
## 20210909 - Recepcionando novos membros da CD
- verificar resposta do Rogério sobre a questão de chaves criptográficas
- Em 10/03/2022 mandei msg pro Deitos para saber se isso andou

___
## 20210903 - Acompanhando a reunião do time
- O Cleiton fez um negócio que já tinha sido definido de outra forma? (Policies x orientações da AWS)

___
## 20210821 - Planejamento do trabalho - De novo
- 

___
## 20210823 - Planejamento do trabalho
- Definições sobre OS para consumo de horas de consultar da AWS levou mais de uma hora
- 

___
## 20210819 - Dedat, Acesso e AWS - repasse do trabalho já realizado
- 

___
## 20210818 - Kickoff Dedat, Acesso e AWS
- Criado projeto no git para acompanhar: https://git.serpro/dedat/acessogovaws
- Criado grupo wpp para comunicação rápida

