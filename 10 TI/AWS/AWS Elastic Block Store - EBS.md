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