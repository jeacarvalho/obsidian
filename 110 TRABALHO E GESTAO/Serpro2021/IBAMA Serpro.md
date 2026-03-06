---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:49.490445+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: arquitetura_geo_analitica_fiscalizacao_madeireira
    weight: 10
    confidence: 0.98
  - name: projeto_floresta_mais_madeira_ibama
    weight: 9
    confidence: 0.97
  - name: solucao_analitica_alertas_fiscalizacao
    weight: 8
    confidence: 0.96
  - name: parceria_transformacao_digital_serpro
    weight: 7
    confidence: 0.95
  - name: contrato_ibama_urc
    weight: 6
    confidence: 0.94
  - name: absorcao_sistemas_ibama
    weight: 8
    confidence: 0.93
  - name: contratos_terceiros_desenvolvimento_software
    weight: 7
    confidence: 0.92
  - name: infraestrutura_aws_suporte_serpro
    weight: 6
    confidence: 0.91
  - name: sistemas_ibama_sisfogo_siga_sca_protocolo_montreal
    weight: 7
    confidence: 0.9
  - name: forca_tarefa_subir_sistemas_estaleiro
    weight: 5
    confidence: 0.89
  cdu_primary: '351.777'
  cdu_secondary:
  - '338.47'
  - '004.4'
  - 351.823.5
  cdu_description: Administração pública. Serviços públicos. Gestão. Organização. Planeamento. Serviços de fiscalização e controlo. Proteção ambiental. Gestão de recursos naturais. Desenvolvimento de software. Contratos de desenvolvimento.
---
___
# 20220503 - Arquitetura Geo Analítica
- Convocada pela SUPAI
- [[Estratégia]] para fazer detalhamento de arquitetura e necessidades tecnológicas para o projeto "Floresta mais madeira" do IBAMA. É o conjunto de iniciativas já em desenvolvimento de painéis
- Em parelalo existe a expectativa de um grande projeto com total relação temática com esses painéis.
- Solução análitica que permite gerar alertas na fiscalização do ciclo completo de um projeto de extração madeireira
- Projeto a ser desenvolvido com empresa parceira através do projeto de "Parceria e transformação digital"
	- Esse processo ainda não teve nenhuma execução no [[serpro]], essa será a 1a
	- Foram descritas as atividades a serem feitas no edital
	- 3 empresas estão qualificadas: stefaninni, Elon group e Mackinse
- Ano passado foram feitas algumas conversas com o Ibama, também pelos parceiros
- RFP - contextualização do que é o projeto e o empreendimento a ser desenvolvido. Apenas stefanini aceitou e seguiu entregando o documento ao Serpro que deve aceitar
	- Mas é uma visão muito macro ainda
- URC está construindo  novo contrato com IBAMA nesse momento.
- O que a SUPAI precisa?
	- No início da RFP foi um desenho extremamente conceitual de alto nível
	- Agora precisa de insumos na proposta de contrato da URC

___
# 20210615 - Nova reunião para absorção
- Janaína dando panorama
	- Encadear as atividades e colocar precedências e definir prazos internos
	- Expectativa é iniciar semana que vem
- Jean citou a possibilidade de AWS
	- Janaína - SERPRO é suporte nesse caso tb?
	- Jean 
		- Imagina que sim, Serpro seria sustentação. Já há pilotos (Min. Saúde, por exemplo)
		- Na visão dele pode ser muito bom para o Serpro. (Eu não sei...)
- Contratos vigentes com 3os de desenvolvimento
	- Datainfo - até 03/2021
- Reforçei necessidade de participação do desenvolvimento do IBAMA nessas reuniões
	- Janaína ficou de levar. Confirmar na próxima reunião

___
# 20210610 - Nova reunião para absorção
- Jean deixou claro que se a terceira que desenvolve para o Ibama não participar, o trabalho vai ser infrutífero
- Filipe (URC) - Contratos de 3os que expiraram foram os que já absorvemos
- Ninguém do domínio de desenvolvimento na reunião - Danielle chegou depois
- SAST e DAST estão previstos?

___
# [[Geo#20210607 - Retomada absorção Ibama]]

___
# 20210302 - Pedido ajuda Fritz e Gustavo
- Relatam muita lentidão após subir o ambiente de desenvolvimento em email enviado hoje.
- São 4 sistemas:
	- [[IBAMA_SISFOGO2_DAS.pdf]]
	- [[IBAMA_SIGA_DAS.pdf]]
	- [[IBAMA_SCA2_DAS.pdf]]
	- [[IBAMA442017_Protocolo_de_Montreal_V3_DAS.pdf]]

___
# Sine die
- Houve uma reunião para tratarmos de força tarefa para subir sistemas no estaleiro, com as notas de chat aqui:[[IBAMA força tarefa estaleiro - notas do chat]]