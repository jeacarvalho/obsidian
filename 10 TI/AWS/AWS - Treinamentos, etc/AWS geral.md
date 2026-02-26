# Mapeando o assunto
- [[Architecting for Security on AWS]]
- [[Architecting for Security on AWS _ Pluralsight]]

AWS geral

Conta root: [jeacarvalho@gmail.com](mailto:jeacarvalho@gmail.com)
IAM: arn:aws:iam::263280154917:user/awsadmin (?)
IAM console login: https://263280154917.signin.aws.amazon.com/console

**Anotando tópicos e conhecimento adquirido, por serviço da AWS**

(lista de serviços obtidas ao consultas grupo do IAM, consultor de acesso. URL: https://console.aws.amazon.com/iam/home?region=sa-east-1#/groups/AWSAdmins)

Amazon IAM

- Sempre procurar criar polices e roles para acessos aos serviços

- Nesse curso o professor cria policy para que o webserver possa acessar o DynamoBD, com permissões específicas (create table, leitura, etc):  https://app.pluralsight.com/course-player?clipId=2a33c5d7-7bf2-4653-b089-ac8ecef19be9

- KMS - Tem administradores da chave, quem pode usar.

Em um curso o tutor recriou um volume de uma instância EC2 e encriptou. Foi necessário copiar e encriptar a cópia. A partir da cópia, ele iniciou nova instância EC2, mas agora apontando para o volume criptografado

Também é possível criptografar buckets na S3

é possível criar policies específicas para permitir apenas acessos mínimos a buckets (OAI - Origin Access identity)

Amazon EC2

- VPC

Criar VPC

Criar subnets

Os ranges de IP precisam ser pensados conforme a necessidade de mais ou menos subnets em uma VPC.

Criar Inet Gway

VPC route table

routes, destination, nova para 0.0.0.0 e o Igatway acima vai tornar a vpc aberta para a internet?

VPC endpoint: em vez de uma VPC sair para outros serviços, como o DynamoDB, via int gatway, pode ser usado esse recurso, que torna a comunicação mais restrita e, assim, mais segura. Aqui é mostrado como:  [https://app.pluralsight.com/course-player?clipId=2a33c5d7-7bf2-4653-b089-ac8ecef19be9

NACL - Netowrk Adress Control List - Whilelists, blacklists

Amazon EC2 Auto Scaling
Amazon EC2 Image Builder
Amazon EC2 Instance Connect

Amazon S3

- Policies,  importante para permitir acesso ou não aos objetos

- KMS se aplica aqui tb

Amazon Route 53
Amazon Route 53 Resolver
Amazon Route53 Domains

Amazon RDS
Amazon RDS Data API
Amazon RDS IAM Authentication

Amazon SNS

AWS Billing

AWS Config

- Notifica, registrando no S3, como a configuração evoluiu através do tempo, notificando mudanças

- https://app.pluralsight.com/course-player?clipId=2a33c5d7-7bf2-4653-b089-ac8ecef19be9

AWS CloudTrail

Amazon CloudWatch
Amazon CloudWatch Logs
Amazon CloudWatch Synthetics

Amazon Athena

- Consultas a conteúdos do S3, a partir de tabelas que devem ser configuradas

- SQL

- Logtrail é uma das possibilidades (https://app.pluralsight.com/course-player?clipId=2a33c5d7-7bf2-4653-b089-ac8ecef19be9)

Alexa for Business
Amazon API Gateway
Amazon AppFlow
Amazon AppStream 2.0
Amazon Chime
Amazon Cloud Directory
Amazon CloudFront
Amazon CloudSearch
Amazon CodeGuru
Amazon CodeGuru Profiler
Amazon CodeGuru Reviewer
Amazon Cognito Identity
Amazon Cognito Sync
Amazon Cognito User Pools
Amazon Comprehend
Amazon Connect
Amazon Data Lifecycle Manager
Amazon Detective
Amazon DynamoDB
Amazon DynamoDB Accelerator (DAX)
Amazon Elastic Block Store
Amazon Elastic Container Registry
Amazon Elastic Container Service
Amazon Elastic Container Service for Kubernetes
Amazon Elastic File System
Amazon Elastic Inference
Amazon Elastic MapReduce
Amazon Elastic Transcoder
Amazon ElastiCache
Amazon Elasticsearch Service
Amazon EventBridge
Amazon EventBridge Schemas
Amazon Forecast
Amazon Fraud Detector
Amazon FreeRTOS
Amazon FSx
Amazon GameLift
Amazon Glacier
Amazon GroundTruth Labeling
Amazon GuardDuty
Amazon Inspector
Amazon Kendra
Amazon Kinesis
Amazon Kinesis Analytics
Amazon Kinesis Firehose
Amazon Kinesis Video Streams
Amazon Lex
Amazon Lightsail
Amazon Machine Learning
Amazon Macie
Amazon Managed Blockchain
Amazon Managed Streaming for Kafka
Amazon Mechanical Turk
Amazon Message Delivery Service
Amazon Mobile Analytics
Amazon MQ
Amazon Neptune
Amazon Personalize
Amazon Pinpoint
Amazon Pinpoint SMS and Voice Service
Amazon Polly
Amazon QLDB
Amazon QuickSight
Amazon Redshift
Amazon Rekognition
Amazon Resource Group Tagging API
Amazon SageMaker
Amazon SES
Amazon Session Manager Message Gateway Service
Amazon Simple Workflow Service
Amazon SimpleDB

Amazon SQS
Amazon Storage Gateway
Amazon Sumerian
Amazon Textract
Amazon Transcribe
Amazon Translate
Amazon WorkDocs
Amazon WorkLink
Amazon WorkMail
Amazon WorkMail Message Flow
Amazon WorkSpaces
Amazon WorkSpaces Application Manager
Application Auto Scaling
Application Discovery Arsenal
AWS Accounts
AWS Amplify
AWS App Mesh
AWS App Mesh Preview
AWS AppConfig
AWS Application Discovery Service
AWS AppSync
AWS Artifact
AWS Auto Scaling
AWS Backup
AWS Backup storage
AWS Batch

AWS Budget Service
AWS Certificate Manager

- para pegar certificados para servidores para informar em ALB (Application Load Balancer)

AWS Certificate Manager Private Certificate Authority
AWS Chatbot
AWS Cloud Map
AWS Cloud9
AWS CloudFormation
AWS CloudHSM

AWS Code Signing for Amazon FreeRTOS
AWS CodeBuild
AWS CodeCommit
AWS CodeDeploy
AWS CodePipeline
AWS CodeStar
AWS CodeStar Notifications
AWS Connector Service
AWS Cost and Usage Report
AWS Cost Explorer Service
AWS Data Exchange
AWS Database Migration Service
AWS DeepComposer
AWS DeepLens
AWS DeepRacer
AWS Device Farm
AWS Direct Connect
AWS Directory Service
AWS Elastic Beanstalk
AWS Elemental MediaConnect
AWS Elemental MediaConvert
AWS Elemental MediaLive
AWS Elemental MediaPackage
AWS Elemental MediaPackage VOD
AWS Elemental MediaStore
AWS Elemental MediaTailor
AWS Firewall Manager
AWS Global Accelerator
AWS Glue
AWS Ground Station
AWS Health APIs and Notifications
AWS Identity and Access Management
AWS Import Export
AWS IoT
AWS IoT 1-Click
AWS IoT Analytics
AWS IoT Device Tester
AWS IoT Events
AWS IoT Greengrass
AWS IoT SiteWise
AWS IoT Things Graph
AWS IQ
AWS IQ Permissions
AWS Key Management Service
AWS Lake Formation
AWS Lambda
AWS License Manager
AWS Managed Apache Cassandra Service
AWS Marketplace
AWS Marketplace Management Portal
AWS Migration Hub
AWS Mobile Hub
AWS OpsWorks
AWS OpsWorks Configuration Management
AWS Organizations
AWS Outposts
AWS Performance Insights
AWS Price List
AWS Purchase Orders Console
AWS Resource Access Manager
AWS Resource Groups
AWS RoboMaker
AWS Savings Plans
AWS Secrets Manager
AWS Security Hub
AWS Security Token Service
AWS Server Migration Service
AWS Serverless Application Repository
AWS Service Catalog
AWS Shield
AWS Snowball
AWS SSO
AWS SSO Directory
AWS Step Functions
AWS Support
AWS Systems Manager
AWS Transfer for SFTP
AWS Trusted Advisor
AWS WAF
AWS WAF Regional
AWS WAF V2
AWS Well-Architected Tool
AWS X-Ray
CloudWatch Application Insights
Comprehend Medical
Compute Optimizer
Data Pipeline
Database Query Metadata Service
DataSync
Elastic Load Balancing
IAM Access Analyzer
Launch Wizard
Manage - Amazon API Gateway
Network Manager
Service Quotas