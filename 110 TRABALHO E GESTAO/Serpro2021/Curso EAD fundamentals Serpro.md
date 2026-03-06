---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:52.583320+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: servicos_geograficos_azure
    weight: 8
    confidence: 0.9
  - name: custos_operacionais_vs_investimento_azure
    weight: 9
    confidence: 0.95
  - name: deducao_impostos_nuvem
    weight: 7
    confidence: 0.85
  - name: comparacao_servicos_nuvem_paas_saas_iaas
    weight: 8
    confidence: 0.92
  - name: regioes_zonas_disponibilidade_azure
    weight: 9
    confidence: 0.96
  - name: limites_assinaturas_azure
    weight: 7
    confidence: 0.88
  - name: gerenciamento_grupos_assinaturas_azure
    weight: 9
    confidence: 0.94
  - name: azure_sentinel_seguranca
    weight: 8
    confidence: 0.91
  - name: azure_key_vault_gerenciamento_segredos
    weight: 8
    confidence: 0.93
  - name: circuitos_expressroute_azure
    weight: 6
    confidence: 0.8
  cdu_primary: '004.7'
  cdu_secondary:
  - '336.2'
  - '658.15'
  cdu_description: Sistemas de computação em nuvem, com foco em infraestrutura, gerenciamento, segurança e aspectos financeiros.
---
- Azure geo
- [[azure-services-6c41a736.png]]
- CapEx x OpEx --> Os caras falam sobre dedução de impostos em cada categoria. Tudo é dinheiro...
- [[ComparaPassSassIass.png]]
- [[regions-azure.png]]
- [There's a minimum of three zones within a single region](https://docs.microsoft.com/en-us/learn/modules/azure-architecture-fundamentals/regions-availability-zones)
- [Subscription limits: Subscriptions are bound to some hard limitations. For example, the maximum number of Azure ExpressRoute circuits per subscription is 10](https://docs.microsoft.com/en-us/learn/modules/azure-architecture-fundamentals/management-groups-subscriptions)
- Vc pode criar uma estrutura flexível de managment groups e Subscription. É flexível, como vc pode ver nessa imagem: ![[management-groups-and-subscriptions-bba71896.png]]
- Limitações quanto aos grupos de gestão: 
	- [Important facts about management groups](https://docs.microsoft.com/en-us/learn/modules/azure-architecture-fundamentals/management-groups-subscriptions)
- [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview)
- Azure Key Vault - Armazenar senhas, tokens, etc...