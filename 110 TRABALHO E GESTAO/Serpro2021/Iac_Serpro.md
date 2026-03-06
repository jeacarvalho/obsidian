---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:53.279206+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: infraestrutura_como_codigo
    weight: 10
    confidence: 0.98
  - name: gerenciamento_de_configuracao
    weight: 9
    confidence: 0.95
  - name: automacao_de_infraestrutura
    weight: 9
    confidence: 0.94
  - name: pulumi
    weight: 8
    confidence: 0.9
  - name: terraform
    weight: 8
    confidence: 0.88
  - name: linguagem_rust
    weight: 7
    confidence: 0.85
  - name: problemas_acesso_rede
    weight: 7
    confidence: 0.92
  - name: segmento_rede
    weight: 6
    confidence: 0.8
  - name: documentacao_faq
    weight: 6
    confidence: 0.85
  - name: runners_corporativos
    weight: 5
    confidence: 0.75
  cdu_primary: '004.7'
  cdu_secondary:
  - '004.4'
  - '004.6'
  cdu_description: Redes de computadores. Protocolos. Gerenciamento de redes. Infraestrutura como Código (IaC) com ferramentas como Pulumi e Terraform, problemas de acesso em segmentos de rede e documentação associada.
---
| links                                                                                                                                                                                               | Arquivos |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [Faq erro acesso sistemas](https://iac.gitpages.[[serpro]]/doc/gestao/faq/#estou-com-problemas-de-acesso-entre-algumas-maquinas-do-iac-no-mesmo-segmento-de-rede-ex-aicrunnershared3-e-maquinas-do-iac) |          |
|                                                                                                                                                                                                     |          |

___
## 20230317 - Pulumi x terraform
- Lendo sobre rust [aqui](https://cloak.software/blog/i-built-startup-in-rust/), encontrei a informação desse Pulumi. Ao falar sobre Iac o autor parece preferir o investimento de tempo no Pulumi e não no terraform

___
#### 20210304 - Peter no [chat.serpro](https://chat.serpro.gov.br/channel/iac?msg=ZCTquoPwi7JacPPjb)
> boa tarde!
Algumas equipes estão reclamando de problemas de acesso entre ambientes que estão dentro do mesmo segmento de rede do IaC em desenvolvimento. Foi registrado na FAQ do IaC o motivo do problema e a solução que deve ser aplicada quando ocorrer este tipo de problema - https://iac.gitpages.serpro/doc/gestao/faq/#estou-com-problemas-de-acesso-entre-algumas-maquinas-do-iac-no-mesmo-segmento-de-rede-ex-aicrunnershared3-e-maquinas-do-iac. Este problema também tem ocorrido para algumas builds que rodam em um dos runners corporativos (aicrunnershared3) com necessidade de acesso a algumas máquinas do IaC em desenvolvimento.

- Nova entrada na faq para tratar problema de acesso entre máquina Iac no mesmo segmento de rede

