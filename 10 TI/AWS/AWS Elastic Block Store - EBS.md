---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:58.277273+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: armazenamento_hdd_vs_ssd
    weight: 8
    confidence: 0.95
  - name: aws_ebs_snapshots_backup
    weight: 10
    confidence: 0.98
  - name: aws_availability_zones_redundancia
    weight: 7
    confidence: 0.92
  - name: aws_regions_redundancia
    weight: 7
    confidence: 0.92
  - name: criptografia_dados_transito_aws
    weight: 9
    confidence: 0.96
  - name: alteracao_volume_aws_on_the_fly
    weight: 8
    confidence: 0.94
  - name: gerenciamento_volumes_aws_ec2
    weight: 8
    confidence: 0.93
  - name: comando_linux_lsblk_verificar_volumes
    weight: 6
    confidence: 0.88
  - name: comando_linux_mke2fs_criar_filesystem
    weight: 6
    confidence: 0.88
  - name: aws_tags_gerenciamento_custos
    weight: 9
    confidence: 0.97
  cdu_primary: '004.6'
  cdu_secondary:
  - '621.3'
  cdu_description: Sistemas de computadores. Armazenamento de dados. Redes de computadores. Serviços de nuvem.
---
- HDD ou SDD - Ainda tem opção de HDD?
	- Sim! SDD para o servidor e os dados. Mas para logs um HDD seria mais barato e atenderia as necessidades
- É possível criar [[AWS EBS snapshots]] - bakcups!
	- E podem ficar em [[AWS Avaibility Zones]] ou até mesmo [[AWS Regions]] diferentes
	- Dados podem ser criptografados para que no trânsito de rede entre o servidor e o volume estejam encriptados. Segurança para usar zonas e regiões diversas
	- Snapshots são recriados no momento de criação do volume
- Se precisar mudar o tipo (de HD para SSD) ou aumentar a capacidade, isso pode ser feito on the fly, sem precisar parar o EC2
- Os volumes são acessados a partir da visão EC2 na console
- Um volume precisa ser criado na mesma [[AWS Avaibility Zones]] do servidor EC2 que vai usá-lo
- Após criar o volume e vinculá-lo ao servidor correto é possível logar via ssh e usar o [[comando linux lsblk]] para verificar os volumes attachados
	- E, escolhendo o volume, é possível criar um sistema de arquivos nele com o [[comando linux mke2fs]]
- Vc pode (e deve) usar as [[AWS tags]], nomeando tudo. Porque vc pode visualizar a conta a pagar agrupando por eles.

anterior:[[AWS Elastic Compute Cloud - EC2]]
próximo:[[AWS Simple Storage Services - S3]]