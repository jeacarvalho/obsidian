---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:53.785132+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: novo_modulo_esapli
    weight: 10
    confidence: 0.98
  - name: recomendacao_tecnologias
    weight: 9
    confidence: 0.95
  - name: integracao_tibco_zapi
    weight: 8
    confidence: 0.92
  - name: acesso_grande_porte
    weight: 7
    confidence: 0.9
  - name: integracao_sispar_parcweb_siefpar
    weight: 8
    confidence: 0.93
  - name: integracao_por_arquivos
    weight: 7
    confidence: 0.91
  - name: milhao_contribuintes_sapli
    weight: 6
    confidence: 0.85
  - name: processo_assincrono
    weight: 7
    confidence: 0.9
  - name: banco_dados_historico_arquivos
    weight: 6
    confidence: 0.88
  - name: endpoint_rest_processamento
    weight: 8
    confidence: 0.94
  cdu_primary: '004.7'
  cdu_secondary:
  - '004.4'
  - '004.6'
  cdu_description: Redes de computadores. Comunicações de dados. Sistemas de informação. Gestão de dados. Processamento de dados
---
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
