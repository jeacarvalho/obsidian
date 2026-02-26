### Descrição: Para tratar assuntos relacionado ao novo e-Sapli

| links | Arquivos |
| ----- | -------- |
|       |          |

___
##### 20210205 - 1a Reunião Arquitetura Gerenciador
- Seria um novo módulo
- Intenção: verificar qual a recomendação de utilização de tecnologias
- Ainda usam tibco no acesso ao grande porte
	- Recomendação: usar ZAPI - Documentação: https://servicos.corporativos.pages.[[serpro]]/migracao.tibco/zapi/
- Integrações com SISPAR, PARCWEB, SIEFPAR
	- Proposta inicial - integrar por arquivos
- Hoje há um milhão de contribuintes na base em toda a vida do Sapli (Fabio Dávila)
- Basicamente:
	- Envia arquivo dos três sistemas
	- Processo assíncrono
		- Uso do ZAPI para acessar grande porte sapli
	- Banco de dados para registro do histórico de arquivos consumidos
	- Endpoint REST com resultado do processamento a ser acessado pelos sistemas SISPAR, PARCWEB, SIEFPAR
	- Conhecer uso: 
		- Tamanho médio dos arquivos de entrada
		- Quantidade de acessos que os sistemas farão nos endpoints REST
