[[AWS]] Certified Cloud Practitioner: All You Need to Know - PluralSight

Regiões, Zonas de disponibilidade e Edge

Regions contém duas ou mais avaiabilty zones (AZ)

Edge locations (Content delivery network. CDN)

CapEx x OpEx

AWS total cost ownership calculator (TCO calcultator)
AWS Simple month calculator
AWS cost explorer

AWS organizations - falcilidade de distribuir custos e pagamentos.

AWS Well arquitected framework

     Operational Excelence , Security, Reliability, Performance efficiency, cost optimization

AWS Disaster Recovery Approaches
     Backup/Restore --> Pilot light --> Warm Standby -> Multi-site

Suporte:
a) AWS Basic Suppot (sem custo mensal)
     Trsuted advisor (7 core checks)

     24*7 - Customer Service (sem prioridade,  sem garantia de quando será o atendimento), Documentation, forum e withepapers

     Personal Health Dashboard

b) AWS Developer Support (29 dólares ao mês, de início. Atrelado ao nível de gasto/infra que vc contratou.  aumenta o custo conforme o aumento na infra)

     Todas do básico
     acesso a engenheiros em horário comercial
     limitado a um contato na organização

c) AWS Business Support (100 dólares ao Mês, mesmo esquema de aumento de custo do developer

     Todos do developer
     Acesso a todos os checks do trusted advisor
     24*7 chat, telefone, email - acessos aos engenheiros de suporte
     Não há limites de quem faz os contatos

d) AWS Enterprise Support (15000 dólares ao Mês, mesmo esquema de aumento de custo do developer

     Todos do business
     Techincal acconut manager (TAM)
     Concierge Support Team

     Não há limites de quem faz os contatos

![Tempos de resposta Suporte AWS.png](a4bbc007c669bfea584692e9af2e37ff.png) ff
Como acessar a AWS:
     Console
     CLI
     AWS SDK

**Network and content delivery services**

- Route 53
    - DNS Server
    - Global e não regional
    - High avaiable - se cai nos EUA direciona par Europa, por exemplo.
- VPC

    -

- Direct connect
    - Datacenter (Premises) --> AWS
    - Tráfego nesse esquema é mais barato na AWS
- API GAteway
- Cloudfront
    - Edge Locations
    - Cliente acessa o que for mais perto geograficamente

    -

- Elastic Load Balancing
    - Pode distribuir carga entre servidores diferentes, mas dentro da mesma região
    - ALB (Application load balancer)

NLB (Network...

    - Classic Load Balancer

**Security on AWS**

- Identity and Access Management (IAM)
    - Free
    - IAM Identities -
        - **usuários** que acessarão recursos da AWS. Separar da conta "root", que usamos para criação de planos e deleção da conta como um todo
        - **Groups** -  grupos de permissão para diversos usuários IAM
        - **Roles** - permissão para uma tarefa
    - Policies - grant permissions
        - JSON
    - Best pratices
        - Multi factor authentication
        - Least preivilege access
- Security in VPC
    - Security groups - firewall like controls
    - Network ACL - Access control list
    - Flow logs
        - Debug
- Security em geral
    - Cloudtrail - log de tudo
    - Shield  - anti Ddos
    - WAF - Fortify?

**Compute Services**

- EC2
    - AMI - Amazon Machine Image - OS e outros softwares
    - Dados
        - Na instância (Caiu perdeu)
        - EBS - Elastic Block Store
    - iniciado em uma VPC
    - Tipos de instâncias
        - Define memory, cpu e storage type
        - Alterações demandam reiniciar
        - Categorias
            - General purpose
            - Compute optimized (ou memory optimized ou storage opt.)
            - Accelarated computing (Machine learning..)
    - Scaling
        - Vertical - + memória, cpu, etc.
        - Horizontal -
            - Auto scalling group
                - mínimo e máximo de instâncias. É o kubernetes em ação, como no estaleiro
                - health check
                - uma ou mais AZ na mesma region
            - ELB
            - Purchase options
                - On demand, conforme sobem as instâncias, por segundo de uso
                - Reserved - prevê o que se usurá  em 1 a 3 anos e se paga adiantado para obter descontos
                    - Demanda consistência e prevista
                - Spot - se estiver abaixo do uso previsto pela Amazon para aquela Region, há um bom desconto para instâncias que sobem
                    - Batch process
            - Conteiner Management
                - Amazon ECS  -
                - Amazon Fargate - os servidores são gerenciados pela AWS
                - ECS for Kubernetes (EKS)

    -

- Lambda
    - Sem nenhuma infra - Serveless
    - Executa e paga
    - 128 MB a 3GB de memória
    - Event driven workflows
- ECS
- Elastic Beanstalk
    - Automatizar o processo de levantar máquinas na EC2
    - não paga por ele. Paga pelo que ele levantar

**File Storage**

- S3 (Simple Storage Service)
    - Buckets (baldes) - permissões, roles, etc..
    - De acordo com a velocidade de recuperação pode ser configurado serviços de diversos custos
        - Default - standard, usado para dados com acessos frequentes
        - Intelligent  Tiered - De acordo com a constância de uso é escolhido a melhor estratégia pela própria infra
        - Standard IA - infrequently accessed data, com mesma resiliẽncia da standard
        - One Zone IA - infrequently accessed data, apenas uma AZ
    - Pelo menos em 3 AZ
- S3 Glacier (para coisas que podem demorar para ser restauradas)
    - BAckups, etc.. Dados que não são acessados mais
    - Regras de ciclo de vida pra arquivar no Glacier automaticamente
    - Regras na figura![Captura de tela de 2020-04-06 15-03-20.png](6223d89f05931e322f0740fd37d6f97c.png)
- File storage services
    - EBS (Elastic Block Store)
        - GPS (General Purpose SSD)
        - IOPS SSD - Low latency app
        - Throughputh Optimized HDD
        - Cold HDD
    - EFS (elastic File System)
        - For linux
        - Multiple AZ
        - Petabytes
        - 2 classes
            - Standard
            - Infrequent access

**Database Services**

- RDS (Relational Database Service)
    - AWS cuida de proviosar, aplicar patches, backup e restore
    - Multiplas AZ
    - Algumas plataformas suportam réllicas de leitura
    - em uma VPC
    - General Purpose SSD ou IOPS SSD
    - Mysql
    - Postgress
    - MariaDB
    - Oracle
    - Sql Server
    - Aurora
- Aurora
- DynamoDB
    - Nosql
    - document DB or key value DB
    - Autpo scalling baseado em configuração
    - DynamoBD accelarator (DAX) - In memory cache
    - 10 trilhões de requisições por dia, 20 milhões de requisições por segundo!
- Redshift
    - DW
    - Pode fazer query no S3 com Spectrum
- Elasticache
    - Memcached and REDIS
    - DB layer cache
    - Sessiom storage
- Database Migration Service

App integration Services

- SNS (Simpĺe notification Service)
    - Pub/Sub message service (tópicos.."kafka")
    - SMS, email and push notifications
- SQS (Simple Queue Service)
    - Filas (Standard and FIFO)
    - 256kb payload
    - 14 dias de vida da mensagem

**Management and governance services**

- Cloudtrail
- CloudFormation
    - Definir infra com templates
    - IAC
    - gerencia dependências.. o que criar primeiro
- CloudWatch
    - Alarmes baseados em métricas que vão ser avaliadas pelos logs do Cloudwatch

    -
**AWS Marketplace**

- Funcionalidades de terceiros para uso na AWS
- Cobrados na fatura da AWS

-
**AWS Snowball**

- Para migrar grandes volumes de informação para a AWS
- Petabytes

**AWS Snowmobile**

- Para migrar grandes volumes de informação para a AWS
- Exabytes
- Um caminhão com um conteiner para levar a empresa, carregar os dados, e levar para um datacenter da AWS