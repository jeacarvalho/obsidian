---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:59.088664+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: ferramenta_linha_comando_aws
    weight: 10
    confidence: 0.98
  - name: interacao_servicos_aws
    weight: 9
    confidence: 0.95
  - name: instalacao_aws_cli_linux
    weight: 8
    confidence: 0.92
  - name: configuracao_aws_cli
    weight: 8
    confidence: 0.9
  - name: geracao_id_secretkey_aws
    weight: 7
    confidence: 0.88
  - name: console_aws_iam_users
    weight: 7
    confidence: 0.85
  - name: credenciais_seguranca_aws
    weight: 7
    confidence: 0.85
  - name: comando_aws_configure
    weight: 6
    confidence: 0.8
  - name: regiao_default_aws
    weight: 6
    confidence: 0.78
  - name: formato_saida_json_aws
    weight: 5
    confidence: 0.75
  cdu_primary: '004.43'
  cdu_secondary:
  - '004.772'
  - '004.89'
  cdu_description: Programas de computador; Sistemas de computadores; Aplicações de computadores; Ferramentas de linha de comando para serviços de nuvem; Gerenciamento de credenciais e configuração.
---
*is an open source tool that enables you to interact with AWS services using commands in your command-line shell.*

fonte: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

Instalando o cliente: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html

Para configurar o cli precisei gerar um ID/secretkey logando na console, IAM, users, seleciona user, credencias de segurança e pedindo para gerar. Depois usei o comando aws configure para informá-los, bem como a região default e o formato de saída default (jsn)

