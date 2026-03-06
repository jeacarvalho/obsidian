---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:54.586807+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: engenharia_de_software
    weight: 8
    confidence: 0.9
  - name: gerenciamento_de_recursos_de_ti
    weight: 9
    confidence: 0.95
  - name: metadados_de_faturamento
    weight: 10
    confidence: 0.98
  - name: codigo_de_servico
    weight: 7
    confidence: 0.85
  - name: cnpj_cliente
    weight: 6
    confidence: 0.8
  - name: numero_de_contrato
    weight: 6
    confidence: 0.8
  - name: coleta_de_consumo
    weight: 9
    confidence: 0.92
  - name: apropriacao_de_custos
    weight: 8
    confidence: 0.9
  - name: faturamento_de_servicos_de_ti
    weight: 10
    confidence: 0.97
  - name: ambiente_vmware
    weight: 7
    confidence: 0.88
  cdu_primary: '004.7'
  cdu_secondary:
  - '657.4'
  - '336.2'
  cdu_description: Gestão de redes de computadores e sistemas de informação; Contabilidade de custos; Finanças públicas
---
1. Time engenharia vai criar nova oferta
2. vMware : Todo recurso que for insumo para faturamento posterior precisa conter os seguintes metadados: codigo-servico; cnpj-cliente; numero-contrato. Todo consumo nesse ambiente será coletado e enviado para apropriação de custos e faturamento pelo bilhetador SUPCD
3. Elementos da oferta que estejam fora do ambiente vMware: verificar se há insumo criado para os elementos. Em não havendo procurar time da Jussiara. 
4. Em existindo insumo, ele já estará sendo coletado por código de serviço no sigecom. O bilhetador SUPCD irá buscar essa apropriação no serpro data e irá usar o consumo para aumentar o valor consumido na console (vcc) que irá subsidiar o cálculo do csb