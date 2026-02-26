| Arquivos relacionados                          |
| ---------------------------------------------- |
| [[Inteligência_Espacial_no_Serpro_v1.0.0.pdf]] |

---
##### 20201218 Reunião internalização sistema SPU (seat7, seat3, Jonas, , Luis Claudio Moreira Teodoro (AICEI/AISMP), alysson.costa@serpro.gov.br, deivi.kuhn@serpro.gov.br)

- Kick off , abrorção de um sistema da SPU
- Documento absorção do cliente: https://docs.google.com/document/d/11UWCW-CW0iNhYcHTdAQ-5mklpjE4lB9ONsu4VIhXkiY/edit

**sobre o sistema**

- GCSIG SPU cadastros, área do sistema no cliente
- dois grandes sistemas: SPUNET - módulo de cadastro de imóveis com edição de polígonos: geolocalização; outra fonte: localizar os imóveis a partir de cep, endereço, etc..
- houve contrato SPU e exército há cinco anos. Postgis
- com troca do secretário especial os projetos foram revisitados e bateram com esse projeto, mas estava em 3o plano da SPU. Portal de transparência, os dados da SPU são planilhados. Cidadão tem que baixar planilha com 750 mil imóveis
- ao tentar tirar necessidade de login mas viram que tinha que mexer no fonte. Pediram consultoria. Arquitetura antiga com GeoServer
- Não tinha gente de java lá para dar manutenção. 
- Aventou possibildiade de usar o externa apontando para os dados da SPU (URC). Temos a base de dados mas há dificuldade de restaurar o banco.
- Necessidade manter ferramenta para poucos usuários internos e trabalhar na divulgação na internet.
- Colocar camada de visualização que permitesse a pesquisa a partir da base 
- Externa não pareceu um produto pronto para isso, conforme análise DIDES domínio SPU
- Decisão: internalizar asis e evoluir para uma solução posteriormente - Posteriormente na reunião foi dito que pode ser que seja outra proposta, uma vez que o cliente conseguiu botar para funcionar lá.
- spunet poderia alimentar a base do geo
- Temos acesso ao git do projeto. Alysson vai tentar coletar mais informações para o documento de absorção.
- cliente assumiu riscos de desempenho no sistema como está.
- email da área de cadastro informou que colocou na internet, estabilizar o ambiente e tirar as autenticações
- https://imoveisfederais.planejamento.gov.br/spin-web/
- Interface frontend é o que? 
- Kuhn - internet e intranet parecem ser dois requisitos diferentes
- **centróide do polígono** (??)
- Cliente mesmo não considera que a arquitetura atual como sendo possível de seguir (Kuhn)
- SUPAI tentando internalizar base no datake (isabela do Saintclair)

**Rodrigo: **

- SPUNET é muito grande. SPUGEO é um dos módulos (que é o objeto dessa reunião, anteriormente era spin-web)
- A consulta (- https://imoveisfederais.planejamento.gov.br/spin-web/) é outro produto. 

---
##### 20201216
Interessados: 

- Thiago Monteiro (SEAT8), SEAT7, Marcos Lacerda, Fábio Barros e Hugo Benício (SEAT3)
- Reunião prevista de internalização de sistema da SPU em 18/12 14h

___
##### 20201214
- Demanda recebida do Jonas em 10/12.
- abeta issue https://git.serpro/dedat/gestao/ciclo2021/-/issues/1 para gestão do tema
- Solicitado aos times DEDAT os nomes de pessoas que detém esse conhecimento
- Solicitado ao Jonas os nomes de pessoas nas outras unidades.
- recebido do Jonas documento com informações dos trabalhos sobre o assunto na SUPAI; [Inteligência Espacial no [[serpro]] v1.0.0.pdf](https://trello-attachments.s3.amazonaws.com/5f6a32d34693773a718ec279/5fd7c77573794428637ca05e/1feb298e96e435901baf757941891650/Intelig%C3%AAncia_Espacial_no_Serpro_v1.0.0.pdf) 
