#### DWBK Isenção

| links | Arquivos |
| ----- | -------- |
|       |          |

##### 20210126
- Flop explicando o estudo que fez e documentou [aqui](https://meet.google.com/linkredirect?authuser=2&dest=https%3A%2F%2Fgit.[[serpro]]%2Fdedat%2Fdeat7%2Fsuporte%2F-%2Fissues%2F10)
- A princípio a proposta 1 abaixo seria a melhor alternativa
- Nova reunião será marcada para 20210209

___
##### 20210119 - Definição do problema: Automatizar leitura de log, carga de sheets

- Com o uso do sistema a performance foi caindo. Telas quebraram inclusive
- Houve reengenharia e cliente demandou indicadores de uso do sistema
- Pegar log de acesso para apresentar ao cliente indicadores de funcionalidades do sistema
- Extraindo pelo HPOO, manualmente, uma vez por semana
- Pentaho (PDI) para fazer transformação com arquivo muito grande
- Datastudio apresenta os resultados
- Necessidade: ou automatizar isso ou gerar solução nova que não demande intervenção manual

**Proposta 1:**

a) Automatizar leitura de log do HPOO - Danilo conhece, demanda cpf e senha pessoal
b) Criar um script que faça o processamento que hoje é feito com Pentaho
c) Automatizar a população das informações da planilha sheets que o datastudio usa

**Proposta 2:** 

a) Filtro de servlet que fique coletando as informações expondo as informações no formato do prometheus
b) Criar um painel grafana no estaleiro e aposentar o datastudio

DEDAT vai estudar item da proposta 2. Nova reunião DWBK Isenção para 