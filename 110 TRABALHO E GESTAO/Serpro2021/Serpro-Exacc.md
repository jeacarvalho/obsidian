| Histórico de documentos                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [https://git.serpro/CDINO/Iniciativas/stacks-nuvem-de-governo/oracle-exacc/-/issues/1](https://git.serpro/CDINO/Iniciativas/stacks-nuvem-de-governo/oracle-exacc/-/issues/1 "https://git.serpro/cdino/iniciativas/stacks-nuvem-de-governo/oracle-exacc/-/issues/1") |
| [https://git.serpro/CDINO/Iniciativas/stacks-nuvem-de-governo/oracle-exacc/-/issues/4](https://git.serpro/CDINO/Iniciativas/stacks-nuvem-de-governo/oracle-exacc/-/issues/4 "https://git.serpro/cdino/iniciativas/stacks-nuvem-de-governo/oracle-exacc/-/issues/4") |
|                                                                                                                                                                                                                                                                     |

## 20241030 - Apresentação relatório final poc solicitado pela SUNIN
- 
___
## 20240916 - Relatório final billing poc
___
## 20240806 - apresentação billing poc
- A máquina do Serpro vira uma dedicated region "serpro"
- IAM - tudo nasce negado
- Tenancy/root compartment = "sua conta"
	- O cliente vai ter um comparment dentro do root compartment
- ![[CompartmentOracleSerproExacc.png]]
- Tem terraform
- [x] Charles oracle ficou de ver apropriação a nível do cluster x nível de database ✅ 2024-10-01
- https://docs.oracle.com/en-us/iaas/api/#/
- https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/taggingoverview.htm#limits
___
## 20240506 - Definição de venda em reunião do sedat
- Exacc vai ser vendido, inicialmente, obrigatoriamente com CSM
___
## 20240503 - Papo com Cardim sobre modelo de negócio
- Tem capacidade para vender? Ou tudo foi licenciado para o FGTS digital?
- 384 cores, mas para cada banco precisa de dois dbnodes
- Mapeado situações complicadas no ponto de vista de segurança e operacional - Cintia
	- Serpro não pode delegar algumas funções para o cliente: Abrir chamado na Oracle - aí o Serpro fica de ping pong entre cliente e Oracle
	- Backup do ambiente - dado do cliente vai para na estrutura do Serpro (Zero data loss)
- Regison - tem particularidades no Exacc que vai impactar modelo de negócios porque tem muito mais intervenção do time do serpro mesmo no ambiente do cliente
___
## 20240502 - Reunião Mary chamando Regison, etc, para estabelecer início de apoio dela na frente
- Conta master serpro, subcontas são as dos clientes
	- vmCluster separados para cada subconta, criados pelo Serpro
	- Cliente só verá sua vmCluster