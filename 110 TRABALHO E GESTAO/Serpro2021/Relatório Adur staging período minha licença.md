Rodrigo da Silva Adur

17:36

14/10 (pedido para validar o banco) + Microsserviço scp foi incluído no ECS + Microsserviço sigepe foi incluído no ECS + Alteração na infra relacionada ao domínios responsáveis pela comunicação interna (microsserviço -> microsserviço) para possibilitar que um microsserviço exponha mais de uma porta + Alteração na infra para possibilitar que um microsserviço tenha mais de um ponto de montagem 15/10 + Microsserviço infoconv foi incluído no ECS + separação dos dados que variam por ambiente

18/10 + Remoção do DNS provisório criado para o microsserviço config - demandou a equipe desenvolvimento gerar nova imagem + Configuração do proxy autenticado no scp + Criação do módulo internet gateway (em desenvolvimento) + Criação do módulo intranet gateway (em desenvolvimento) + Investigando problema com os redirects nestas soluções de gateway

19/10 + Investigação do problema com os redirects nestas soluções de gateway > Solução geral para este problema é manter esses cenários deredirecionamento no path raiz do gateway + Impossibilidade de implementar o allow/deny list no resource policy do API Gateway privado. > Esta solução terá de ser reescrita usando o WAF. + Alteraçlão de alguns headers usados na comunicação entre o API Gateway e o ALB > Substituição do X-Forwarded-Host pelo Host de forma a manter o DNS usado pelo cliente

20/10 + Ajustes em algumas configurações do microsserviço scp + Microsserviço api-parametrizacoes-v1 foi incluído no ECS + Microsserviço api-clientes-v1 foi incluído no ECS + Microsserviço api-contas-v1 foi incluído no ECS

21/10 + Investigar problema que ocorre com o swagger [https://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html) [https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#passthroughBehavior](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#passthroughBehavior) [https://stackoverflow.com/questions/59516717/aws-api-gateway-adding-content-type-header-to-options-reques](https://stackoverflow.com/questions/59516717/aws-api-gateway-adding-content-type-header-to-options-reques) [https://coringar.hopto.org/swagger/base-espelho/swagger-ui.html](https://coringar.hopto.org/swagger/base-espelho/swagger-ui.html) [https://coringar.hopto.org/api-contas-v1/contas/v1/docs/index.html](https://coringar.hopto.org/api-contas-v1/contas/v1/docs/index.html) Bom

Rodrigo da Silva Adur

17:38

21/10

Bom dia pessoal, segue andamento das atividades no dia 20/10: + Reestruturação/evoluções no módulo gateway + Microsserviço pcturescalingv1 foi incluído no ECS + Microsserviço contas-bff foi incluído no ECS + Microsserviço contas (frontend) foi incluído no ECS + Observações: > Os frontends estão buscando os recursos no raiz, o que inviabiliza reaproveitar o domínio da forma como eu estava fazendo > Para subir este serviço foi necessário criar outro domínio (meu último da cota :-/) > Preci

samos definir e providênciar a criação dos domínio, assim como o certificado que deverá estar no Certificate Manager de forma que eu possa criar os Custom Domain Names apropriados > Estou ajustando e revisando algumas configurações com o Macapuna

Rodrigo da Silva Adur

17:39

22/10 + Ajuste do microsserviço config para contemplar o ambiente da AWS > -Centralização das configurações do módulo config no repositório da equipe (estava sendo usado um repositório temporário) > -Todas as configurações dos microsserviços que estão migrando passaram para o ambiente aws-s > -Ajuste em todos os microsserviços levados para AWS para lerem deste novo diretório do módulo config

+ Testes dos microsserviços > -Macapuna realizou diversos cenários de testes envolvendo os módulos que foram levados para o ECS > -Analise e acompanhamento dos logs > -Ajustes diversos conforme os problemas foram aparecendo + Evolução do módulo gateway > -Tratamento do allow/deny list no gateway privado

25/10 Bom dia, o dia 25/10 foi utilizado para a realização de refatorações diversas: + Padronização do nome dos headers customizados com o prefixo `x` > -Após ler o conteúdo da [RFC 6648]([https://www.rfc-editor.org/rfc/rfc6648](https://www.rfc-editor.org/rfc/rfc6648)) a adoção desta abordagem foi desconsiderada > -Revisitar a padronização dos nomes dos recursos criados > -Nós usamos internamente a conversão ${ambiente}-${cluster}-${microsservico_name} para a identificação de inúmeros recursos > -Ao migrar alguns microsserviço

> -Alguns recursos não podem começar com `aws*`. Desta forma foi necessário alterar a configuração (no módulo config) de todos os módulos migrados para adotar o padrão `s-aws` no lugar de `aws-s` > -Todos os microsserviços migrados foram alterados para obter as configurações deste lugar `s-aws` + Padronização do nome dos microsserviços para ficar exatamente igual aos módulo do estaleiro > Atualização e republicação do módulo config para reapontar todas as dependências entre os microsserviço

Rodrigo da Silva Adur

17:41

para os novos domais com o nome padronizado

Rodrigo da Silva Adur

17:49

Informamos que você esta inscrito no curso Plataforma Kafka que inicia no dia 03/11. Data de realização: 03/11: 9:30 ao 12:00 e 13:00 as 17:30 04/11: 9:30 ao 12:00 e 13:00 as 17:30 05/11: 9:30 ao 12:00 e 13:00 as 17:30 No dia 27/10/2021, às 15h, faremos um teste de acesso e a preparação do ambiente para o curso. Com relação ao link do teste de acesso, estou aguardando a empresa me encaminhar. Assim que receber envio para vocês.