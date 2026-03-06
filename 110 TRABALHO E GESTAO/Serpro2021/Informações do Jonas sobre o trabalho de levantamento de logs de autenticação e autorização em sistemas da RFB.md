---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:50.302017+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: plano_aperfeicoamento_logs_acesso_sistemas
    weight: 10
    confidence: 0.98
  - name: auditoria_cgu_recomendacao
    weight: 8
    confidence: 0.95
  - name: armazenamento_logs_infraestrutura_serpro
    weight: 7
    confidence: 0.9
  - name: retencao_logs_cinco_anos
    weight: 6
    confidence: 0.85
  - name: avaliacao_armazenamento_logs_rfb_aplicacao
    weight: 7
    confidence: 0.92
  - name: mecanismos_logs_sistemas_rfb
    weight: 8
    confidence: 0.93
  - name: implantacao_modulo_analise_logs_gestao_configuracao
    weight: 9
    confidence: 0.96
  - name: plataforma_ingestao_analise_eventos_logs
    weight: 9
    confidence: 0.97
  - name: rastreabilidade_logs_versionamento_publicacao_sistemas
    weight: 8
    confidence: 0.94
  - name: uso_apis_wso2_conecta_gov
    weight: 7
    confidence: 0.88
  cdu_primary: '004.65'
  cdu_secondary:
  - '004.77'
  - '004.62'
  - '351.74'
  cdu_description: Gestão de sistemas de informação. Armazenamento e análise de logs. Auditoria e controle governamental. Segurança da informação.
---
[10/11 15:39] Maria Amelia Franca de Macedo
 

Conforme recomendação 2 de auditoria do CGU foi elaborado um Plano de Aperfeiçoamento de Logs de Acessos a Sistemas. Segue o progresso físico das ações que compõem o plano:
- (i) Avaliação de armazenamento de Logs de Acesso de Sistemas na camada de infraestrutura: 100%
O [[serpro]] armazena todas as logs de requisições de acesso a todos seus servidores de produção com retenção de 5 anos
- (ii) Avaliação de armazenamento de Logs de Acesso de Sistemas da RFB na camada de aplicação: 0%
Prazo: 30/11/2021

Categorizar os sistemas por mecanismo de logs  
- E-CAC   
- Senha rede  
- Senha Sief  
- Pucomex  
- outro (qual log de acesso tem) descrever os logs em cada mecanismo/uso e-lel

- (iii) Implantação do módulo de análise dos Logs de Gestão de Configuração: 100%
O Projeto tem o objetivo de estruturar uma plataforma de ingestão e análise de eventos de logs. Em sua primeira versão, implementou a rastreabilidade de logs de versionamento e publicação dos sistemas , conforme demonstrado no painel de acompanhamento de ingestões em anexo.


 

- (iv) Implantação de melhorias das Logs de Acesso de Sistemas da RFB na camada de aplicação: 0%
Prazo será definido após a avaliação do item (ii)
Prazo de Atendimento do Plano de Aperfeiçoamento de Logs de Acessos a Sistemas
31/03/2022
% de Atendimento das ações do Plano de Aperfeiçoamento de Logs de Acessos a Sistemas
60%

vi, tb, que as apis usam:
via WSO2 e conecta gov, onde é gerado um login e senha 
 
