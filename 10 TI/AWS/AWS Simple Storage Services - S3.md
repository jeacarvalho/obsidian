---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:58.943693+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: servico_armazenamento_nuvem_gerenciado
    weight: 10
    confidence: 0.98
  - name: escalabilidade_armazenamento_objetos
    weight: 9
    confidence: 0.95
  - name: acesso_via_http_s
    weight: 8
    confidence: 0.92
  - name: api_simples_armazenamento_recuperacao
    weight: 7
    confidence: 0.9
  - name: armazenamento_database_snapshots
    weight: 6
    confidence: 0.88
  - name: controles_seguranca_aws_vpc
    weight: 8
    confidence: 0.93
  - name: regioes_aws_armazenamento_replicado
    weight: 7
    confidence: 0.91
  - name: acesso_aws_console_cli_sdk
    weight: 9
    confidence: 0.96
  - name: copia_arquivos_aws_cli
    weight: 7
    confidence: 0.89
  - name: acesso_instancia_ec2_bucket
    weight: 6
    confidence: 0.87
  cdu_primary: '004.73'
  cdu_secondary:
  - '004.67'
  - '004.69'
  cdu_description: Armazenamento em nuvem, serviços de rede, sistemas de computação distribuída
---
- Serviço gerenciado de armazenamento em nuvem
	- Gerenciado - vc não se preocupa em gerenciar os discos envolvidos, nem em qual servidor está. Vai mandando os objetos e a AWS se vira
- Pode armzenat trilhões de objetos e recebe picos de milhões de solicitações por segundo.
	- vc armazena objetos. Podem ter dimensões enormar como terabytes e são acessíveis via http/s
- API simples para armazenamento e recuperação de objetos
- Ideal (?) para armazenar database snapshots (terabytes, lembra?)
- COntroles avançados de segurança. Vc pode configurar para ser acessível somente para sua [[AWS Virtual Private Cloud - VPC]]
- Quando um bucket é criado ele é associado a uma [[AWS Regions]] específica. E cada objeto enviado é armazenado em múltiplos "locais" dessa região. 
- É possível acessar via [[AWS console]], [[AWS CLI]] ou [[AWS SDK]] ou diretamente via os endpoints
	- Exemplo de endpoint: "https://nomedobucket/endpointespecificoregiao/chavedoobjeto"
- é possível copiar arquivos de seu computador via CLI: 
	- (um a um) aws s3 cp demo.txt s3://enderecobucket/nomearquivo
	- (diretório) aws s3 sync algumdiretorio  s3://enderecobucket/nomediretorio
- Ao logar na instância EC2 é possível acessar, mas para visualizar é preciso fazer uma cópia do bucket para o diretório da instância
- Depois de copiado para o bucket é possível alterar permissões, etc, via console web
	