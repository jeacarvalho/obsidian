Architecting for Security on AWS

Protecting AWS Credentials

- CIA - Confidencialidade (ACL), Integridade (DB seguro), Avaliabilty
- Proteger storage, computing and network
- Levels of security
    - AWS services bem configurados
    - OS ok na instância EC2
    - Aplicações
    - Proteger:
        - Credenciais
        - Capturar e analisar logs
        - Redes
        - Data armazenada (in rest)
            - Criptografia
            - Permissões
        - Data trafegando (in transit)
            - Cirptografia
        - Configurar backup, replicação e recovery