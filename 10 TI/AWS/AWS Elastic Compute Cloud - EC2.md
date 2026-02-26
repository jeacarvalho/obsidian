- Elástico - se configurado corretamente, a infra pode crescer ou diminuir conforme necessidade
- Compute - São máquinas linux (por exemplo) onde vc pode colocar qualquer software servidor que desejar, claro, cuidando da aplicação de patches e todos os aspectos de segurança
- Cloud - são recursos hospedados em uma nuvem. No caso do EC2, nuvem AWS

O uso é por instâncias, máquinas que são criadas conforme a necessidade. Essas instânicas são chamadas [[AMI]], Amazon Machine Image. E que podem ser localizadas em qualquer [[AWS Regions]] 

Essas instâncias podem ser criadas via Console, onde podemos selecionar qual a [[AMI]] iremos usar. Pela console pode-se selecionar se são máquinas da própria AWS ou do marketplace, criadas por terceiros. Instâncias linux t2.micro são elegíveis à camada de gratuidade [[AWS free tier]]. No wizard é possível configurar as questões de rede e [[VPC]] Virtual Private Network. Também é aqui que informamos as questões de armazenamento. Também definimos o [{Security Group}], o conjunto de regras de firewall que controla o tráfico para a instância sendo criada. Ao final do processo é criado um par de chaves para acessar a instância via SSH


Previous:[[AWS Cloud Practitioner Essentials - AWS Core Services]]
Next: [[AWS Elastic Block Store - EBS]]