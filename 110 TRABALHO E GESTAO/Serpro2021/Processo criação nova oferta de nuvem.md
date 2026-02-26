Processo criação nova oferta de nuvem

2.1) O time define que será necessária a aquisição de uma máquina especializada. O fornecedor tem como modelo de comercialização do “comodato” e, assim, essa máquina terá um custo mensal para a empresa a ser previsto como custo.  

2.2) O time define que irá usar o Kafka e, avaliando o licenciamento da ferramenta, verifica que seu uso é livre de custos. Mas que, dado o cenário de suporte necessário ao produto, será necessário contratar um fornecedor especializado. Esse fornecedor prevê em seu modelo de comercialização a cobrança de um valor por tópico criado na infraestrutura do ambiente Kafka a ser suportado. 

2.3) O time, junto com a área estratégica da empresa, define que essa infra e o software serão mantidos pelo time de banco de dados da empresa. A partir disso, o time da solução envolve o time de banco de dados, estimando quantas horas mensais de suporte serão necessárias para manter a solução.  

2.3) O time define que a estratégia de apropriação do consumo será a criação de metadados por tópico criado. Ou seja, cada tópico kafka irá conter o código de serviço relacionado, de maneira que seja possível extrair as informações de consumo segregada por cliente/serviço.   

2.4) O time aciona a área de criação de insumos de custos da empresa. Reuniões são realizadas para entendimento da solução e o time de criação de insumos chega a um insumo de custos de “unidade de tópico”, definindo que, dado o cenário do comodato e do suporte contratado, a unidade tem um custo de R$ 500,00 mensais 

2.5) O time aciona a área de criação de novos produtos da empresa, informando o novo insumo de custo e seu valor. A partir disso, a área de criação de novos produtos realiza pesquisas de mercado para entender como os outros providers de nuvem cobram o uso de fila, avalia a margem de lucro definida pela empresa, impacto de impostos, etc, e define que o preço a ser cobrado será de R$ 650,00 

2.6) O time da solução envolve a equipe do billing da solução de nuvem e informa o novo insumo e seu preço de venda. O time do billing cadastra as informações e identifica a api que deverá ser usada pelo time da solução para enviar o consumo da nova solução. 

2.7) O time da solução cria a automação necessária para extrair o consumo, com base na métrica e na unidade de medida, por cliente/código de serviço e enviar, via a api disponibilizada no passo anterior, o consumo do período. 

2.8) O sistema de billing, a partir do consumo enviado e do preço cadastrado, envia diariamente o valor financeiro do consumo para o sistema de faturamento da empresa e a quantidade consumida do insumo para a o sistema de apuração de custos da empresa. Em ambos os casos as informações são organizadas por código de serviço 

2.9) Em paralelo a todo esse processo, o código de serviço 12345, interno à empresa, é criado para alocar mensalmente as horas necessárias dos times de suporte. Essa alocação será revisada periodicamente pelos gestores responsáveis, de maneira a manter uma alocação adequada ao nível de serviço contratado. Veja que tal alocação foi prevista no passo 2.3 acima, e o custo relacionado foi levado em consideração no preço do insumo “unidade de tópico”. Ou seja, a alocação registrada no código do serviço 12345 não será usada no processo de faturamento, por essas horas já estarem precificadas. As horas serão usadas no processo de revisão anual de preços. O time de preços da URC fará o levantamento anual para avaliar se o planejado no passo 2.3 está próximo do que foi alocado no código 12345 e, caso exista alta discrepância o custo do insumo, bem como o seu preço, deverá ser revisto.