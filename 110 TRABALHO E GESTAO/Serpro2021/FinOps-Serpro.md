---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:52.183014+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: turbonomic_ibm
    weight: 8
    confidence: 0.9
  - name: poc_cnj
    weight: 7
    confidence: 0.85
  - name: gerenciamento_custos_cloud
    weight: 9
    confidence: 0.92
  - name: otimizacao_recursos_cloud
    weight: 10
    confidence: 0.98
  - name: machine_learning_infraestrutura
    weight: 7
    confidence: 0.88
  - name: analise_fluxo_componentes
    weight: 8
    confidence: 0.89
  - name: identificacao_gargalos_infra
    weight: 8
    confidence: 0.91
  - name: sobre_dimensionamento_ambiente
    weight: 7
    confidence: 0.87
  - name: vmware_aria_operations
    weight: 6
    confidence: 0.75
  - name: cloudhealth_vmware
    weight: 6
    confidence: 0.78
  cdu_primary: '004.77'
  cdu_secondary:
  - '004.7'
  - '658.15'
  cdu_description: Gestão e otimização de recursos em nuvem, com foco em custos e desempenho, utilizando machine learning e análise de infraestrutura.
---
## Assuntos relacionados
- [[Serpro Cloud One]]
- [[Billing Cloud One]]

___
## 20230928 - Papo inicial com Jonas, Pedro Muller e Lobinho
- Turbonomic, Produto da IBM: https://www.ibm.com/br-pt/products/turbonomic
- Pedro Muller e Joaquim Carvalho dando um panorama da poc que está em andamento com ele.
- CNJ seria o cliente da Poc
	- Foi questionado muito o quanto invasivo a ferramenta seria
- Muller entendeu que um outro caminho haveria e foi par ao kubernetes, para testar
	- Ferramenta tem capacidade de apresentar o fluxo de todos os componentes para mostrar o quanto impacta no custo (?)
		- mostra gargalos e sobre dimensionamentos
	- usa machine learning e vai evoluindo conforme o tempo passa coletando as informações
	- vai até o nível do host e, avaliando, propõe aumento ou diminuição do ambiente
	- (vmWare tb tem o aria operations (antigo vRealize))
- Jonas compartilhou: https://cloudhealth.vmware.com/
- 