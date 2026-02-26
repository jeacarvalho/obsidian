#### fonte: [[aws202001]]:
- Uma nuvem "minha" dentro da nuvem AWS
- uma VPC existe em uma [[AWS Regions]]. Isso quer dizer que uma VPC pode englobar duas [[AWS Avaibility Zones]]? Pela apresentação do vídeo, sim: "Sub redes permitem que a VPC abranja várias avaiabilty zones" 
- Uma VPC pode conter sub redes, e tabelas de rotas podem controlar o tráfego entre elas.
- A partir de um [[AWS Internet Gateway IGW]] é possível dar acesso a uma VPC pela internet e um [[AWS NAT Gateway]] permite que os recursos de uma sub rede privada acessem a internet (INGRESS x EGRESS ? parece que [sim](https://aviatrix.com/learn-center/cloud-security/egress-and-ingress/https://aviatrix.com/learn-center/cloud-security/egress-and-ingress/)

#### fonte: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html: 
- Amazon VPC is the networking layer for Amazon EC2
- Enables you to launch AWS resources into a virtual network that you've defined
