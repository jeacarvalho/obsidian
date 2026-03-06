---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:58.474728+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: computacao_em_nuvem_aws
    weight: 10
    confidence: 0.98
  - name: instancias_computacionais
    weight: 9
    confidence: 0.95
  - name: amazon_machine_image
    weight: 8
    confidence: 0.92
  - name: regioes_aws
    weight: 7
    confidence: 0.88
  - name: console_aws
    weight: 7
    confidence: 0.85
  - name: camada_gratuita_aws
    weight: 6
    confidence: 0.8
  - name: rede_virtual_privada_vpc
    weight: 6
    confidence: 0.78
  - name: grupos_de_seguranca_firewall
    weight: 5
    confidence: 0.75
  - name: acesso_ssh
    weight: 5
    confidence: 0.7
  - name: armazenamento_em_nuvem
    weight: 5
    confidence: 0.65
  cdu_primary: '004.7'
  cdu_secondary:
  - '004.4'
  - '004.6'
  cdu_description: Sistemas de computação em nuvem, redes e infraestrutura de TI
---
- Elástico - se configurado corretamente, a infra pode crescer ou diminuir conforme necessidade
- Compute - São máquinas linux (por exemplo) onde vc pode colocar qualquer software servidor que desejar, claro, cuidando da aplicação de patches e todos os aspectos de segurança
- Cloud - são recursos hospedados em uma nuvem. No caso do EC2, nuvem AWS

O uso é por instâncias, máquinas que são criadas conforme a necessidade. Essas instânicas são chamadas [[AMI]], Amazon Machine Image. E que podem ser localizadas em qualquer [[AWS Regions]] 

Essas instâncias podem ser criadas via Console, onde podemos selecionar qual a [[AMI]] iremos usar. Pela console pode-se selecionar se são máquinas da própria AWS ou do marketplace, criadas por terceiros. Instâncias linux t2.micro são elegíveis à camada de gratuidade [[AWS free tier]]. No wizard é possível configurar as questões de rede e [[VPC]] Virtual Private Network. Também é aqui que informamos as questões de armazenamento. Também definimos o [{Security Group}], o conjunto de regras de firewall que controla o tráfico para a instância sendo criada. Ao final do processo é criado um par de chaves para acessar a instância via SSH


Previous:[[AWS Cloud Practitioner Essentials - AWS Core Services]]
Next: [[AWS Elastic Block Store - EBS]]