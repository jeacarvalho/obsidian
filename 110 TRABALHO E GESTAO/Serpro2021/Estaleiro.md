### Descrição:

| links                                                                                                                                                         | Arquivos |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --- |
| [nova norma certificados](https://solucoes.corporativo.[[serpro]]/sinor/arquivos/DS%20SUPSE%20RE%20002%202019.pdf)                                                |          |     |
| Normativo de uso do estaleiro - [SEGURANÇA DE AMBIENTE DE CONTÊINERES EM NUVEM PRIVADA](https://solucoes.corporativo.serpro/sinor/documento.php?cod=MzY5MjY=) |          |     |
|                                                                                                                                                               |          |     |

___
#### 20210922 - Mudança de certificado no estaleiro
- [Planilha com módulos que precisam ser alterados](https://docs.google.com/spreadsheets/d/1Aw6pvaShXT6qWRPAjPXGGlckgnybtEjYrqw61IwHkyM/edit#gid=0)
- [Planilha cópia com possíveis módulos RJO](https://docs.google.com/spreadsheets/d/15gE1THmfsX3auNfLq8vrh3mqgOIIZu8U9vyY5SiO1ao/edit#gid=0)

___
#### 20210604 - Apresentação das mudanças por João Morais
- Por que uma alteração em que o pai da criança diz que "muitas pessoas vão ficar perdidas, achando que tem que aprender estaleiro de novo"?
##### JM apresentando as mudanças
- Mudança básica - exposição de Ingress mudou completamente
- "Não mexa no produtivo até que vc esteja ciente do que está acontecendo"
- Domínio virtual deixa de existir. Grupos e gateway vai suprir isso
- Novos elementos: gateway e grupos de segurança
	- Grupos - conjunto do que tem hoje de configuração de whitelists. Vai estar associado oa gateway
	- gateway é "o cara da novidade"
		- Coisas do ambiente e módulo vieram pra cá

___
#### 20210604 - Internalização time sispar e apidue

___
#### 20210409 - Atualização da console
- #done 20210409 ler https://docs.estaleiro.serpro.gov.br/noticias/post/2021-04-09-atualizacao-console/
___
#### 20210224 - Apresentação pelo Misael do ambiente de IA no estaleiro
- ![[IAEstaleiro1.png]]
- Equipamentos GPU para o estaleiro
- 3 Poweredge C4140 - 1 em treinamento e 2 em Inferência
- 4 GPUS NVIDIA Tesla V100
- Tem pipeline de IA com Runner no Gitlab
- Novos flavors de IA
- ![[MLOpsEstaleiroIA.png]]
- Há limitação porque a placa GPU não permite particionamento de CPU
- ![[IAEstaleiroTecnologiasHomologadas.png]]

___
##### 20201211 - Nova norma para solicitação certificados estaleiro
Norma anterior foi cancelada.
Norma atual (Supse-re-002/2019) : https://solucoes.corporativo.serpro/sinor/arquivos/DS%20SUPSE%20RE%20002%202019.pdf

Apesar de falar sobre assinatura de código DEDAT não será mais o responsável pelos certificados no estaleiro.

Enviado email para Cadu e Stamato, os únicos que eu gerenciava o vencimento dos certificados...: Assunto Sobre certificados no estaleiro	11 de dezembro de 2020 11:46

