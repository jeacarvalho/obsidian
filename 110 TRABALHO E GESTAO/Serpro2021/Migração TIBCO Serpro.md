---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:53.477562+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: migracao_tibco_pucomex
    weight: 10
    confidence: 0.98
  - name: gerenciamento_licencas_software_tibco
    weight: 9
    confidence: 0.95
  - name: suporte_contratual_tibco
    weight: 9
    confidence: 0.94
  - name: capacidade_suporte_cd
    weight: 8
    confidence: 0.9
  - name: alternativas_mensageria_activemq
    weight: 8
    confidence: 0.88
  - name: analise_sistemas_utilizando_tibco
    weight: 7
    confidence: 0.85
  - name: monitoramento_projetos_migracao
    weight: 7
    confidence: 0.87
  - name: mensageria_nats_alto_volume
    weight: 6
    confidence: 0.8
  - name: documentacao_migracao_tibco
    weight: 6
    confidence: 0.82
  - name: gestao_contratos_software
    weight: 5
    confidence: 0.75
  cdu_primary: '004.77'
  cdu_secondary:
  - '004.42'
  - '004.62'
  cdu_description: Redes de computadores. Protocolos de comunicação. Sistemas de mensagens. Gerenciamento de software. Migração de sistemas.
---
# Descrição:

Para acompanhar o assunto

| links                                                                                                                                    | Arquivos |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [Documentação mínima](https://servicos.corporativos.pages.[[serpro]]/migracao.tibco/)                                                        |          |
| [melhorias na apresentação das informações](https://gitcorporativo.serpro/servicos.corporativos/migracao.tibco/-/issues)                 |          |
| [Acompanhamento dos projetos de migração](https://datastudio.google.com/reporting/56cdf847-49ff-46a1-a2bf-688dea60fa26)                  |          |
| [Planilha com projetos a migrar](https://docs.google.com/spreadsheets/d/1jUuvJ8g7OuIPcFfxvLFfBI-UUrR_8y2ZP8xLpVCD46s/edit#gid=434017977) |          |
| [Cana do chat para acompanhar](https://chat.serpro.gov.br/channel/tibco)                                                                 |          |

## 20210329 - [[Dominios#20210329 - Pucomex migração tibco]]
- CD e capacidade de suporte


##  20210318 - Apresentação Rene na semanal DEDAT
- Em torno de 180 sistemas usando tibco
- WSMQ - Não tem licença para os 180. Se todos forem, demanda alteração de contrato.
- Tibco software é eternamente do Serpro
	- Mesmo sem contrato de suporte pode ser usado o software
	- Mas sem contrato não teremos suporte e não poderá ser feita nenhuma nova instalação do Tibco
	- Hoje temos 800 clientes levantados nas jvm.
	- Não podemos criar nem novas filas
- o Acompanhamento será feito na planilha de projetos a migrar (link acima)
- Meta GDES dos gestores
- **Monteiro**: SUPCD tem projeto de uso do ActiveMQ.
	- **Rene**: 
		- WSNQ não é "a verdade" para todos. Vai melhorar o texto da documentação sobre a migração
		- SEDAT pode colocar outras opções para os sistemas
		- Mas ele não teve contato com estudo de forma corporativa de uso do ActiveMQ
- **Jonas**: Se tivermos melhorias na documentação, sugerir. Rene diz "ok"
- **Deitos**: Tem sistema usando NATS no estaleiro com 60 milhões de mensagens dias. **Rene**: Coisa pra caramba!
 

___
## 20210302 - Envio de email pelo Bisotto


