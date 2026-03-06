---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:59.593225+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: gerenciamento_identidade_acesso_aws_iam
    weight: 10
    confidence: 0.98
  - name: monitoramento_auditoria_aws_cloudtrail
    weight: 9
    confidence: 0.97
  - name: monitoramento_alertas_aws_cloudwatch
    weight: 9
    confidence: 0.97
  - name: protecao_ddos_aws_shield
    weight: 8
    confidence: 0.96
  - name: gerenciamento_configuracao_aws_config
    weight: 8
    confidence: 0.96
  - name: otimizacao_recursos_aws_trusted_advisor
    weight: 7
    confidence: 0.95
  - name: escalabilidade_automatica_aws_auto_scaling
    weight: 7
    confidence: 0.95
  - name: arquitetura_serveless_aws
    weight: 8
    confidence: 0.94
  - name: redes_virtuais_aws_vpc
    weight: 9
    confidence: 0.96
  - name: seguranca_redes_aws_security_groups_acls
    weight: 8
    confidence: 0.95
  cdu_primary: '004.8'
  cdu_secondary:
  - '621.37'
  - '621.39'
  cdu_description: Tecnologia da informação. Sistemas de computadores. Redes de computadores. Segurança de redes. Serviços de computação em nuvem.
---
Architecting for Reliability on [[AWS]] (Pluralsight)

Key Concepts and Core Services

- IAM
    - Authentication com usuário e senha ou com chaves programáticas (ProgrammaticKeys)
        - Também pode ser feita com roles. Uma ação recebe uma role em vez de ser validade com usuário e senha ou programatic keys
    - Request informa a ação e onde ela será executada (action and resource)
    - Com esse request, será buscada uma autorização (authorization), validada em umm access policy
    - Criar grupos de policies...
        - usuário awsadmin, pass: awsadminjeacarvalho
            - Link para console: https://263280154917.signin.aws.amazon.com/console
    - MFA  - Multi factor authentication - instalado o google authenticator. E associado ao usuário raiz
- CloudTrail
    - 90 dias. Se quiser mais, cria seus próprios trails
- Cloudwatch
    - Habilitar alertas faturamento
- AWS Shield
- AWS Config
    - Pode colocar regras para avaliar em um dashboard se o ambiente como um todo está de acordo com o previsto
- Trusted advisor
    - Permite acompanhar o uso de recursos em sua conta frente a limites pré estabelecidos pela AWS, como, por exemplo, limite de ips para vpc ou ec2, por região

Architecting for Reliability on AWS

- Auto scaling group - lança novas instâncias ao aumentar a carga
- Serviços em vez de servidores
    - managed services
        - RDS
        - S3
        - DynamoDB
        - ELB
    - Servelsse architecture
        - Lambda
        - API Gateway
        - S3
        - Cloudfront

Architecting Reliable Virtual Networks

- VPC overview da arquitetura do projeto de exemplo

![Captura de tela de 2020-04-15 15-19-47.png](b49e553f9bc21d0267391af8c697c867.png)

- Atenção ao criar estruturas
    - NAT gateway é cobrado por hora. Então, fique atento
    - as private net precisam apontar para seus NAT gatwaye
    - Uma VPC, duas AZ, 3 subnets para cada tema em  cada AZ.
    - Elastic ip para os dois NAT gatway
    - Ao criar o EC2 nas duas AZ, testou com rum command, com ping de dentro para o dns google 8.8.8.8
    - Teve que criar rule para permitir que o comando fosse executado de dentro da instância
- Security groups permitem criar regras que se apliquem a diversos elementos
- ACL - Access control lists
- Configurou regras. ExternalGroup para o ELB e InternalGroup para os EC2. Os do EC2 só recebem http e https e apenas de quem esteja no ExternalGroup. O externalgroup só recevbe http e https mas de qualquer ip (aberto)
- Executou comandos nos servidores EC2 para instalar o apache e iniciar os serviços lá