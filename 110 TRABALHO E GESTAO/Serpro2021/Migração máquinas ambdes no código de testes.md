#### Descrição:
Há máquinas do pucomex, slaves jenkins e máquinas windows de testes

Código	Domínio	Subdomínio	Servidor	Status	Local
08169	-	-	linux2pucomex	RUNNING	OPENSTACK
08169	-	-	linux3pucomex	RUNNING	OPENSTACK
08169	-	-	linux4pucomex	RUNNING	OPENSTACK
08169	-	-	slave2rjo	RUNNING	OPENSTACK
08169	-	-	slaverjo	RUNNING	OPENSTACK
08169	-	-	teste_rjo	RUNNING	OPENSTACK| 


| links                                                                   | Arquivos |
| ----------------------------------------------------------------------- | -------- |
| [Acompanhar migração](http://migracao.dev.[[serpro]]/)                      |          |
| [Painel ambdes atualizado](https://portal.dev.serpro/ambdes/login.html) |          |

___
##### 20210326
- Máquina testes windows removidas, conforme [essa issue](https://git.serpro/devops/aicat/demandas/-/issues/5238) e [essa](https://git.serpro/devops/ambdes/demandas/-/issues/756#note_699978)
___
##### 20210126
- Máquina testes windows desligadas
> parece que passou a quebrar um job. Warley abriu uma issue: https://git.serpro/devops/aicat/demandas/-/issues/5238
- Slaves jenkis que estavam parados foram excluídos. (anotação do warley na [issue](https://git.serpro/devops/ambdes/demandas/-/issues/696#note_634649))

Conforme anotado nesta issue [https://git.serpro/devops/ambdes/demandas/-/issues/756#note\_592567](https://git.serpro/devops/ambdes/demandas/-/issues/756#note_592567), a conexão master + slave tem mais de mês.

___
##### 20210125
- Mandei email informando que o desligamento será feito amanhã


___
##### 20201214
- Mandei email para o pessoal que usa a máquina windows para teste

---
##### 20201204
Email Leandro (BHE) mostrando que tem job do Mauro rodando no slave de lá:

Pessoal,

com o objetivo de desativar as VMs do AmbDes que estão como slave no Jenkins, gostaríamos de solicitar a ação por parte das equipes de desenvolvimento que possuem jobs em execução no slave linux.teste.bhe.selenium. 

Favor realizar a desativação dos seus jobs ou configuração para utilização de outro slave. Como a maioria dos jobs está com falha, acredito que o mais natural seja a desativação dos mesmo.

Próximos passos:
- Desconexão do slave no Jenkins: 14/12/2020
- Desligar a VM no AmbDes: 21/12/2020
- Excluir a VM no AmbDes: 28/12/2020

Segue a lista de sistemas com jobs ativos, juntamente com o líder responsável pelo mesmo:
PreCadin - Maria Cristina Breve Gomes Garcia
Fibra-Cálculo - Carlos Eduardo de Jesus
Pucomx COAD - Mauro Cabral Agostinho

Para acessar a lista de jobs ativos: https://jenkins2.aic.serpro/computer/linux.teste.bhe.selenium/builds

---
##### 20201202
Warley:
Cesar e Jose Eduardo.

Vou inativar os agent slaves linux1.rjo e linux2.rjo, e redirecionar os label para o agent slave linux5.

Também criei seguinte issue abaixo, para acompanhamento desta ingerência, caso ocorra a necessidade de alguma intervenção recorrente em atividades de build neste agente slave linux1.rjo e linux2.rjo.

- https://git.serpro/devops/aicat/demandas/-/issues/4968
- https://git.serpro/devops/aicat/demandas/-/issues/4969

___