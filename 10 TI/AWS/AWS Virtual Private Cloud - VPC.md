---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:59.142347+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: rede_virtual_aws
    weight: 10
    confidence: 0.98
  - name: configuracao_rede_aws
    weight: 9
    confidence: 0.95
  - name: zonas_disponibilidade_aws
    weight: 8
    confidence: 0.92
  - name: sub_redes_aws
    weight: 8
    confidence: 0.93
  - name: roteamento_trafego_aws
    weight: 7
    confidence: 0.9
  - name: acesso_internet_aws
    weight: 7
    confidence: 0.88
  - name: gateway_internet_aws
    weight: 6
    confidence: 0.85
  - name: gateway_nat_aws
    weight: 6
    confidence: 0.86
  - name: ingress_egress_aws
    weight: 5
    confidence: 0.8
  - name: camada_rede_ec2
    weight: 5
    confidence: 0.82
  cdu_primary: '004.77'
  cdu_secondary:
  - '004.451'
  - '004.6'
  cdu_description: Redes de computadores. Redes virtuais. Redes em nuvem. Configuração e gerenciamento de redes. Segurança de rede.
---
#### fonte: [[aws202001]]:
- Uma nuvem "minha" dentro da nuvem AWS
- uma VPC existe em uma [[AWS Regions]]. Isso quer dizer que uma VPC pode englobar duas [[AWS Avaibility Zones]]? Pela apresentação do vídeo, sim: "Sub redes permitem que a VPC abranja várias avaiabilty zones" 
- Uma VPC pode conter sub redes, e tabelas de rotas podem controlar o tráfego entre elas.
- A partir de um [[AWS Internet Gateway IGW]] é possível dar acesso a uma VPC pela internet e um [[AWS NAT Gateway]] permite que os recursos de uma sub rede privada acessem a internet (INGRESS x EGRESS ? parece que [sim](https://aviatrix.com/learn-center/cloud-security/egress-and-ingress/https://aviatrix.com/learn-center/cloud-security/egress-and-ingress/)

#### fonte: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html: 
- Amazon VPC is the networking layer for Amazon EC2
- Enables you to launch AWS resources into a virtual network that you've defined
