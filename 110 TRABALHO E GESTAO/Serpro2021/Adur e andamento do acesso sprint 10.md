[[Acessogov AWS SERPRO]]
# Consulta no kanban:
- https://kanban.serpro.gov.br/?controller=BoardViewController&action=show&plugin=&project_id=4382&search=status%3Aopen+assignee%3ALeandro

## Adur
- 167774 - Criação dos gateways privados
	- restringir ips da VPN intranet do [[serpro]] como tb homeoffice (VPN)
	- Ontem reunião com Azize e Giovani que customizou infra para possibilitar acesso via vpn, desde que esteja em um grupo específico. Hoje funcionou
	- [6:03 PM] Rodrigo da Silva Adur - Reunião com o Giovanni, Reinaldo e Azize         
	- Configuração da infraestrutura para possibilitar o acesso ao api gateway via VPN         
	- Configuração da minha conta da VPN para conclusão dos grupos necessários para a comunicação mencionada acima             
	- Consultoria com  Azize
		-  Realização de Laboratório para validar a solução do private api gateway
	-  Adur vai começar a implementar essa solução
-  167775 - Adur tentar pegar
-  167777 - Adur
-  166944 - Adur junto com Giovani
-  CI/CD - tem trabalho com Bastos
	-  Adur entende que deveria ter 3 issues: uma de definição e duas de execução, uma para renato no RHSSO e outra no time SEDAT

## Hugo
-  166938 - Automatização dos configs dos micros serviços **Equipe desenvolvimento** Maca vai pegar depois de 167370 - João foi para LDAP. 
-  167761 - "Teste de microsseriviços" **Equipe desenvolvimento**
-  167370 - Criação dos scripts RNF dos microsserviços **Equipe desenvolvimento**
	- Hugo em 17/02 1- Script de RNF para avaliação de desempenho dos fluxos básicos (no caso o escolhido foi o cadastro) Atualização: Macapuna retomou hj a atividade e amanhã (HOJE, 18/02) finalizará o fluxo interno (atual de produção). Na segunda iniciará as customizações para o ambiente da AWS. Estimamos finalizar até quarta (23)
-  167778 - Executar teste de RNF - microsserviços - Renato com RHSSO e **equipe de desenvolvimento**
-  166910 - Automatizar a troca de URL do ambiente de Staging TTL já ok
	-  Parametrizar as URL dos micros serviços de Front End	- **Equipe desenvolvimento**, João, fazer e testar
-  166871 - Ajuste na configuração dos dashboards do grafana **Equipe desenvolvimento**
- Não mapeado issue -  Carga LDAP: Raimbow Table dos registros da v2_cidadao com base64(hash512) para fazer join com "ecidadao.senha_expirada" - Jõao fazendo agora
- Planilha de acompanhamento de suas ações: [Migração Acesso para RHSSO+AWS.xlsx (sharepoint.com)](https://serprogovbr-my.sharepoint.com/:x:/r/personal/laudemira_farias_serpro_gov_br/_layouts/15/Doc.aspx?sourcedoc=%7B541A80B8-B9AF-4CEF-A3CB-7FFD329E8321%7D&file=Migra%C3%A7%C3%A3o%20Acesso%20para%20RHSSO%2BAWS.xlsx&action=default&mobileredirect=true&cid=5f9f21d9-b6ad-4b18-95d5-76e43ece85ad)

## Tarefas no kanban sem visibilidade de andamento e ciência:
- 166938 - Automatização dos configs dos micros serviços (Precisa verificar com time de desenvolvimento (Hugo) como está o andamento. Depende tb da liberação do RHSSO.)
- 166910 - Automatizar a troca de URL do ambiente de Staging, Parametrizar as URL dos micros serviços de Front End
- 167165 - Definir a estratégia para o FDW do BD de relatório com LDAP (A definição da estratgia foi feita. Faltando operacionalizar a estrategia. Deitos vai ver com o Hugo. Devido ausencias e eventos criticos nos ultimos dias, não foi possivel nessa sprint. Hugo pediu mais pessoas pra apoiar. Deitos vai ver alguem de outra divisao pra apoiar. Essa atividade é muito importante para gerar relatorios gerenciais mas não imprescindivel. Não impede o fluxo operacional da aplicação)
- 166871 - Ajuste na configuração dos dashboards do grafana (linha 12 na planilha?)



### Relato wpp 20220217

2-Ações de implementação de RHSSO
a) Senha expirada - atualizar valor no LDAP: corrigido
b) Erro no envio de email (feedback messages/OTP): corrigido
c) Desbloqueio de contas (cenário de excesso de tentativas): em execução (previsa: 17/2)
3-Criação de json de carga da entidade Cliente(MitreId para RHSSO)
-> atualização: será finalizada amanha (17)

A iniciar
1) Construir script para integracao da base LDAP(cidadao) para tabela de Relatorios
3) Auditoria kafka: infoconv 
4) Auditoria kafka: sigepe 
5) Auditoria kafka: gestão
6) Auditoria kafka: empresas(bff e APis)

## Pendências
-  166943 - Adur já fez mas depende que alguém passe as políticas gerenciadas pela AWS
	-  Quem deveria passar? Giovani
	-  Provisionar waf já ok
	-  Quebrar criando outra para "incorporar as políticas gerenciadas pela AWS" com Giovani
-  167165 - Deitos ficou de ver se Jonas consegue alguém. Mandou email
-  165582 - Adur já fez e passou para Reinaldo aplicar as tags. Mas depende de decisão de começar a pagar
 
 # Diárias 
 
 ## 18/02/2022
 - Reinaldo
	 - Bastions com problema. Bloqueio retirada dos nats
	 - URL de certificado do SSo com problemas na produção? Reinaldo não identificou e vai ver com Renato
	 - Pendência na conta de validação configurar attachs no transit gateway - alguém compartilhou e talvez agora consiga fazer
	 - Route 53 comando para atualizar, precisa id vpc
	 - Sugere Hugo a usar p-aws para teste RNF 
- Renato
	- RHDS RHSSO disponíveis prontos para serem integrados aos microserviços
	- Testes em relação aos bancos em staging
	- Hugo repassou lista de clients a cadastrar, lista de Staging
	- Bug no keycloak
	- Elissandro: Esse bug impacta bastante para Renato. 
- Ie
	- Vai instalar pg crypto na aws... a pedido do Hugo
-  #done Task DMS com Deitos? Azize
- Hugo pediu rotina mágica que lê arquivo e grava na aws: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PostgreSQL.S3Import.html

- API Gateway para filtrar serviços
- Estaleiro dentro da infra com Ips das duas fontes, intra e inter. Na AWS não temos mais isso, porque só tem Ip da internet
	- ALB seria a solução mas tem limitação de regras, Teria que pedir aumento de quotas
	- WAF seria a solução, mas demanda DNS privado, que traz impacto na visão do time de desenvolvimento
- Ye aguarda script do Hugo de banco - Carga LDAP: Raimbow Table  (João fazendo)

## 22/02/2022
- Colocando Staging no ar corretamente depois de diversas alterações
- Reunião com time e Azize e solução definida
-  #done Pendência com segurança Giovani vendo como materializar: VPN Home office e Via SERPRO
	- Equipe desenvolvimento tem que alterar algumas questões em grupos de segurança
- 166943 - Separar
- Email do Adur com solução de regras:
	- Para viabilizar essa solução (origem home office), o Giovanni se encarregou de verificar: 
		- A melhor forma de direcionar o tráfego AWS dos funcionários que se encontram em home office, logados na VPN, para a rede do SERPRO. 
		- Verificar o acesso dos clintes que acessam nossos sistemas por meio do Via SERPRO.

### Ie
- Conexões abertas 20 na aws sem atividade. Replicação acontecendo? Está sincronizando? 
	- Reinaldo: duas tasks, produção e RNF. Estão funcionando mas não atualizou
	- Quem está com isso no time de cá??? Deitos que vinha conduzindo DMS
- Aguardando scripts do Hugo para continuar migração de dados para LDAP
- Tem script de consulta em produção rodando no HPOO há um bom tempo

### Reinaldo
- Implementando scripts de provisão do Opensearch para ambiente de produção
	- Deitos disse que SUPAI faria integração com elastic??
- Migração a micro serviços para ambiente de monitaração, corrigido configuração na conta de monitoração
- Ambiente de validação pendente de propagação de rotas da parte de Giovani fazer autorizações
- Ticket porta 25 na AWS - pediram para exemplificar caso de uso e foi registrado no ticket
	- Ficando preocupado com o suporte porque está demorando bastante.
- Crédito ainda pendente de liberação
- #done  Revisão do security groups com Giovanni - Pendente parte de banco de dados/Reinaldo

### Wilton
- DIretor quer saber o que vai para AWS e o que fica no Serpro
- Wilton quer uma topologia mostrando tudo o que é "anexo" a esse processo. Deitos já tinha pedido ao Hugo. #done reunião agendada

### Hugo
- Preocupação com carga de LDAP. 
	- Um banco à parte do gerenciado AWS para ter LDAP no Postgre

### Renato
- Aguardando teste RNF do ponto de vista do RHSSO
- Tratando integração de federação com os bancos
	- Precisa de ajuda do Giovani para criar regras
- BUG do RHSSO - ticket aberto no suporte da Red Hat


# 23/02/2022
## Giovani
- https --> levantar outro listener na porta 443
- imagens estaleiro não tem o módulo de tls incorporados nas imagens, precisa regerar imagens
	- Necessidade de regerar já era esperado
- Precisa acontecer antes de entrar em produção
- Aprovado necessidades para a alteração de acessos (VPN Serpro e VIA Serpro

## Reinaldo
- tickets aws de porta 25 foram atendidos
- componentes compartilhados projeto terraform já adpatado para monitoração

# 24/02/2022
## Adur
- Giovani materializar o que é necessário para a nova estrutura de regras.. Novos grupos
-  Imagens base do estaleiro para tls -> quem vai atualizar as imagens base? Tem que reunir para definir quem vai fazer (comunicação com https..)
- WAF - quebrar - regras gerenciadas tem que ser uma issue separada.
- Revisão questões de segurança andou mais um pouco
- Macapuna e Adur deixando Staging liso
- Microserviço de configuração - negócio
	- Macapuna customizou agora
- Script testes: pronto pra estaleiro; aguardando produção aws para finalizar aqui..

## Reinaldo
- Cluster elastic provisionado - issue bloqueada aguardando teste

## Renato

# 25/02
## Adur
- Apoiando equipe nas configurações
	- 166938 - Equipe responsável, Adur com eles
- 166944 - Refinando quando dá, muito melhor mas ainda tem coisa
- 167370 - Prontos apontando para estaleiro, finalizando p-aws apontar para lá: amanhã deve deslanchar
- 166943 - WAF, pronto nossa parte
- 166938 - Macapuna faendo com apoio do Adur
- 166910 - Falta Renato fazer as tarefas - vai mudar os domínios? 
	- Foi feito o processo de alterar os domínios?
	- #166934 issue para virada de chave
- 167165 - Com João
- 166871 - Pendente
- 167775 - Adur fazendo hoje - Em andamento
- Staging ok --> Focar nas funcionalidades alvo do RNF
	- Aplicado em produção
		- 5 horas tentando resolver um problema que era no RHSSO
- Finalizando, Macapuna vai para finalização de script e outro tem que vir para finalizar
- Solicitar máquina EC2 ao Reinaldo para a SUPAI - abri issue no git

# 02/03/2022 - Review
- Staging não funcional
- Crise no BC time acesso
- Fechamos estratégia de segurança
- Funcionalidade do elastic começou a andar
- 167775 - Adur fazendo hoje - Em andamento
- 167778 - Depende da finalização da 167370
- 166944 - (Contínua) Refinando quando dá, muito melhor mas ainda tem coisa
- 167370 - Prontos apontando para estaleiro, finalizando p-aws apontar para lá: amanhã deve deslanchar
- 166938 - Macapuna fazendo com apoio do Adur
- 166910 - Falta Renato fazer as tarefas - vai mudar os domínios?
- 167165 - Com João (trabalhosa)
- 166871 - Pendente
