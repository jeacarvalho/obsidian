[[Contabilidade]]
[[Economia]]
# Bibliografia
## Disponibilizados no AVA
- [[EST_ebook_Walter_Sande.pdf]]
- [[EST_ebook_Adriana_Tostes.pdf]]
## BÁSICA 
- BONAFINI, F. C. (Org.). Estatística. São Paulo: Pearson Education do Brasil, 2012. Biblioteca Virtual. https://plataforma.bvirtual.com.br/Acervo/Publicacao/182728
- CRESPO, A. A. Estatística fácil. 19. ed. São Paulo: Saraiva, 2009. LARSON, R.; FARBER, B. Estatística aplicada. São Paulo: Pearson, 2010. Biblioteca Virtual. 
- SANDE, Walter. Estatística. Rio de Janeiro: Ilumno, 2017. (Ambiente Virtual de Aprendizagem).[[EST_ebook_Walter_Sande.pdf]]
## COMPLEMENTAR
- LAPPONI, Juan. Estatística usando Excel. Rio de Janeiro: Campus, 2005. (Minha Biblioteca). 
- LEVIN, J.; FOX, J. A.; FORDE, D. R. Estatística para ciências humanas. 11. ed. São Paulo: Pearson, 2012. Biblioteca Virtual. 
- MCCLAVE, J. T.; BENSON, G. P.; SINCICH, T. Estatística para administração e economia. 10a edição São Paulo: Pearson, 2009. Biblioteca Virtual.  https://plataforma.bvirtual.com.br/Acervo/Publicacao/402
- MORETTIN, L. G. Estatística básica: probabilidade e inferência. São Paulo: Pearson, 2010. Biblioteca Virtual. 
- WALPOLE, Ronald. Probabilidade & Estatística para engenharia e ciências. 8ª edição. São Paulo: Pearson Prentice-Hall, 2009. (Biblioteca Virtual)


# Unidade 1 - Introdução ao estudo estatístico
## Introdução
- o trabalho da Estatística contempla 
	- o **planejamento** da pesquisa, 
	- a **coleta** de dados, 
	- a **organização** dos dados para gerar informação, 
	- a **interpretação** e 
	- a **análise** desses dados e 
	- a **apresentação** de resultados de forma que possam subsidiar processos de tomada de decisão mais razoáveis. 
- A Estatística se ocupa do **tratamento de dados** de maneira que possa **extrair informações** desses dados.
	- estatística **descritiva**, trata da maneira como podemos **apresentar (descrever) um conjunto de dados** organizados em tabelas e gráficos, e sua **síntese** por meio de medidas estatísticas. Essas medidas são classificadas como **medidas de posição**, que incluem a média, a moda e a mediana, e **medidas de dispersão**, que incluem a variância, o desvio-padrão e o coeficiente de variação
	- estatística **inferencial** fundamenta-se na teoria das **probabilidades** para **estabelecer conclusões** sobre um grupo inteiro, denominado população, podendo utilizar-se somente da observação de uma parte desse todo, denominado amostra.

## Aula 1 - Estatística no Brasil e no mundo
### Definições
- **Dados**: valores assumidos pela variável observada
- **Informação**: o que informa, o que taz dados que podem ser unidos a outros criando um conhecimento diferente do que tínhamos
- **Variável** de interess: característica de interesse que pode assumir diferentes valores de indivíduo a indivíduo
	- Tipos de variáveis
		- Quantitativa
			- Discreta: números inteiros (pags de livro, qt pessoas fila) e finitos (confoem ebook walter p. 13)
			- Contínua: fracionários (temperatua, peso) e infinitos (confoem ebook walter p. 13)
		- Qualitativo
			- Nominal: identidades e identificadores diversos
			- Ordinal (ordem): faixas de classificação: pequeno, médio, grande..
- **População**: considerada no Censo.. Apenas... o resto é:
- amostra parte da população (parte x todo)
- índices e indicadores
	- índice: a partir de dados gerados ao longo do tempo
		- IDH, por exemplo. Proposto pela ONU. A partir de dados censitários do IBGE (2010, último)
			- Contrapondo o [[PIB]] que só calcula crescimento econômicos
			- média geométrica: multiplica valores e extrai a raiz da quantidade de valores. Se 3 índices, raiz cúbica da multiplicação dos índices
				- Era média aritmética mas isso mascarava diferenças brutais
		- IBOVESPA
		- IPCA, IGP-M
	- indicadores: alvo, onde quero chegar
- Ciência de dados
	- BI, Bigdata


## Aula 2 - Elaboração e análise de gráficos e tabelas
- Retoma classificação das variáveis

### Dados brutos
> são os dados na forma em que foram coletados, sem nenhum tratamento (aula 2)
- A organização desses dados nos leva às tabelas

### Tabelas
- Há uma [norma ABNT](https://biblioteca.ibge.gov.br/visualizacao/livros/liv23907.pdf) para representar dados em tabelas. (aula fala de norma ABNT mas o arquivo é do IBGE sem identificar qual é o número da norma)
	- A ABNT NBR 14724 orientar a aplicação da norma IBGE
- **ROL**: organizarmos os dados brutos em ordem crescente. Mas dados repetidos tem importância. Distribuição de frequências na tabela ajuda a resolver isso, criando classes, com informações de limite inferior e superior
- Frequência absoluta - nr de vezes que aparece na amostra
- Frequência relativa - nr de vezes que aparece na amostra/total amostra
- Tipos de gráficos a usar: [[UVA_Estatistica_resumo_tipos_graficos.pdf]]

## Aula 3 - Medidas de posição e dispersão
### medidas de síntese
- também chamadas de medidas **descritivas**, são utilizadas para resumir os dados de uma variável **quantitativa**, representando o conjunto por meio de valores **numéricos**. 
	- posição (média, moda e mediana) e 
	- dispersão (amplitude, variância, desvio-padrão, coeficiente de variação).
- parâmetros: se forem calculadas a partir de “dados populacionais”
-  estimadores ou estatísticas : se forem calculadas a partir de “dados amostrais”

### Medidas de posição (tendência central)
-  resumo e caracterização de um conjunto de dados
-  Um resumo das medidas: [[UVA_Estatistica_resumo_medidas_posicao.pdf]] - o título do arquivo está errado
	-  Média
		-  Aritmética
		-  Ponderada
		-  Geométrica: raiz do número de variáveis
	-  Mediana
	-  Moda
	
### Medidas de dispersão
- Segundo livro Walter Sande, p. 28:
> As medidas mais frequentemente usadas são a **amplitude, a variância e o desvio médio padrão** e servem para medir a representatividade da média
- Quanto maior forem os valores de desvio-padrão e coeficiente de variação, menos representativa será a média (aula 3)
	- Se o coeficiente de variação for superior a 50%, há alta dispersão, o que aponta heterogeneidade dos dados
- [[UVA_estatistica_resumo_medidas_dispersao.pdf]]
	- Amplitude total
	- Variância
	- Desvio padrão
	- Coeficiente da variação

> Para comparar a variabilidade entre grupos por meio do desvio-padrão ou da variância, os conjuntos de dados têm que possuir o **mesmo número de observações, a mesma unidade de medida e a mesma média** (aula 2)

# AVA1
- ![[Confirmacao envio AVA 1 Estatistica UVA.png]]

# Unidade 2 - Probabilidade
## Aula 1 Introdução à probabilidade
- Tratar com problemas onde a incerteza está presente. Quase tudo na vida, praticamente.
- Modelos envolvem o conceito de chance

### Experimento aleatório e espaço amostral
>**Experimento aleatório:** é a delimitação do que se pretende observar dentro do contexto de probabilidade.
**Espaço amostral:** é o conjunto que identifica os resultados possíveis quando observamos um determinado experimento aleatório. É identificado pela letra **S** (de _space_) ou pela letra grega **Ω** (ômega).

- Livro Sande: 
	- processo de coleta de dados associados a um fenômeno em que obtemos resultados distintos e não previsíveis com certeza absoluta é chamado de **experimento aleatório**.

### Evento e probabilidade
- Evento: É qualquer subconjunto de um espaço amostral S de um determinado experimento aleatório.
- A probabilidade de ocorrência de um evento A de um espaço amostral S de um determinado experimento aleatório é caracterizada por P(A)
	- Quando P(A) = 0, dizemos que **A é um evento impossível**, pois não há nenhuma possibilidade de ele ocorrer.
	- Quando P(A) = 1, dizemos que **A é um evento certo**, uma vez que ele certamente irá ocorrer.

### Cálculo da probabilidade
#### 1º caso: probabilidade teórica com eventos equiprováveis
- P(A) = n(A)/n(S)
	- n(A) = número de elementos de A
	- n(S) = número de elementos de S
	- Seja A = resultado é ímpar para o lançamento de um dado de seis faces - n(A) = 3 (1, 3, 5)
	- n(S) = 6 (todos os lados)
	- P(A) = 3/6 --> 0,5

#### 2º caso: probabilidade teórica com eventos não equiprováveis
- Jogar um dado duas vezes e observar a soma das faces que saíram. Há 3 combinações que podem somar 4 (1 + 3), (2+2), (3 + 1), quanto só uma combinação soma 2 (1, 1). Assim, os eventos não são equiprováveis.
- P(A) = número de casos favoráveis à ocorrência de A - n(A) / número de casos possíveis n(S).
	- No exemplo de somar 4 --> n(A) = 3; n(S) = 36; 3/36 --> 1/12
	- No exemplo de somar 2 --> n(A) = 1; n(S) = 36; 1/36

#### 3º caso: probabilidade empírica usando frequência relativa
- Soma do espaço amostral x soma total
- CAso de cursos e gêneros. Administração, 250 mulheres, 100 homens, etc...
- Somar total por curso, total por gênero e total geral. Total geral sempre será denominador e totais relativos irão variar no numerador conforme as perguntas.

## Aula 2 Conceitos de probabilidade
- atributos de ocorrência dos eventos (E) são denominados de **axiomas da probabilidade**

#### Eventos complementares
- Espaço amostral S. Evento A x evento complementar ~A; 
	- A soma de A e ~A = S
	- P(A) + P(~A) = 1
		- P(A) = 1 - P(~A)

#### Eventos mutuamente exclusivos ou mutuamente excludentes
- Dizemos que os eventos A e B são mutuamente exclusivos quando a ocorrência de um impede a ocorrência do outro

#### Probabilidade da união
- P (A ∪ B) = P (A) + P (B) - P (A ∩ B)
	- Isso quando A e B tiverem elementos em comum, ou seja, quando A e B não são mutuamente exclusivos, isto é, quando A∩B≠∅
	- Quando não há intereseção, soma-se somente.

### Eventos independentes
- Dizemos que os eventos A e B são independentes quando a ocorrência de um não interfere na ocorrência ou não do outro
	- _P (A ∩ B) = P (A) . P (B)_


## Aula 3 Probabilidade condicional (probabilidade condicionada)
- Estamos agora interessados na probabilidade de ocorrência do evento A condicionada à ocorrência do evento B (ou probabilidade de A, dado B; ou probabilidade de A, se B), cuja notação é P(A|B), sendo:
	- P (A | B) = P (A intersec B)/ P (B)

# Unidade 3 - Distribuição de probabilidades
## Aula 1 -  Variáveis aleatórias e distribuições de probabilidade 
- O conjunto de todos os resultados possíveis é chamado de **espaço amostral**, e costumamos denotá-lo por _Ω_. Desta maneira, _Ω={A1∪A2∪A3 }_.
- Associamos cada valor de X à sua probabilidade. Essa associação é chamada de “**distribuição de probabilidade**” da variável aleatória X. Sendo assim, uma distribuição de probabilidade descreve os possíveis valores da variável aleatória a ela relacionada, assim como suas probabilidades
### Variáveis aleatórias discretas
- Uma variável aleatória é classificada como “discreta” quando possui um conjunto enumerável (finito ou infinito) de valores possíveis.
> Imaginemos, agora, que haja interesse em estudar a chegada de carros a uma praça de pedágio numa rodovia, num intervalo de uma hora. Sendo X = quantidade de carros que chegam em um intervalo de uma hora, essa variável aleatória pode assumir qualquer valor inteiro não negativo. Não sabemos, a priori, qual é o maior valor possível, mas podemos enumerar facilmente esse conjunto

### Variáveis aleatórias contínuas
- uma variável aleatória é chamada de contínua quando o conjunto de valores possíveis é infinito, não enumerável

### Cálculo de probabilidades com variáveis aleatórias
#### Função de probabilidade – variáveis discretas
- A distribuição de probabilidade de uma variável aleatória discreta é chamada de “função (massa) de probabilidade”
- _P(X < 3) = P(X = 0) + P(X = 1) + P(X = 2)_
- Probabilidade de algo acontecer = 1 - P(não acontecer)
#### Função densidade de probabilidade – variáveis contínuas
- não faz sentido calcular _P(X = a)_ ou _P(X = b)_, a probabilidade de _X_ estar no intervalo entre _a_ e _b_ pode, também, ser expressa por _P(a≤ X ≤b)_

### Média ou valor esperado
> E(X), é uma medida que dá uma ideia de qual valor de X que seria esperado, caso o experimento ao qual a variável está associada fosse repetido inúmeras vezes
- para uma variável aleatória discreta: 	
	- ![[MediaVariavelDiscretaEstatisticaUVA.png]]
- Para variável contínua:
	- ![[MediaVariavelContinuaEstatisticaUVA.png]]

### Variância
- é uma medida de sua dispersão estatística, e corresponde ao valor esperado do quadrado de quanto ela se afasta de seu valor esperado
- Para variáveis discretas: _Var(X) = E [(X-E(X))2] = E (X2 ) - [E(X)]2_
- Para variáveis contínuas: ![[VarianciaVariavelContinuaEstatisticaUVA.png]]

## Aula 2 - Distribuição de probabilidade discreta: Binomial e Poisson
### Distribuição Binomial
> não é incomum ser mais importante saber não apenas a probabilidade de ocorrência de um único resultado, mas de uma combinação de várias repetições do fenômeno que leva a eles
> Se o cliente recusar o lote de 1000 peças caso haja mais de dez peças defeituosas, será que a probabilidade de haver problemas é muito alta?
> Esse fenômeno é modelado perfeitamente pela **Distribuição Binomial**, e a variável aleatória discreta associada à situação descrita é _X = quantidade de peças defeituosas em um lote de 1000 unidades_.
> A **variável aleatória** do fenômeno de interesse é, então, a quantidade de vezes, dentre as n repetições do fenômeno base, em que o resultado correspondeu a “sucesso” --> _X~Bin(n; p)_
- A função de probabilidade da Distribuição Binomial é dada por: ![[FuncaoProbabilidadeDistribuicaoBinomial.png]]


### Distribuição de Poisson
> é adequada para modelar fenômenos quando não estamos interessados exatamente na quantidade de sucessos em uma determinada quantidade de repetições, mas na frequência de sucessos, calculada pela quantidade de sucessos em um determinado intervalo de tempo ou distância
- Segundo aula gravada pela professora (https://www.youtube.com/watch?v=TiO_HlIQrCU), trata-se de uma distribuição de variável discreta em intervalo contínuo
- ![[FuncaoProbabilidadeDistribuicaoPoison.png]]

## Aula 3 - Distribuição de probabilidade contínua: Normal
- ![[DistribuicaoProbabilidadeContinuaNormal_estatitiscaUVA.png]]
- Precisamos da média e do desvio-padrão
	- E(X)=μ
	- Var(X)=σ2
- Quando aumentamos o valor da média, deslocamos o gráfico para a direita. 
	- Se diminuirmos, o gráfico desloca-se para a esquerda. 
- Quando o desvio-padrão é grande, a curva é larga, espalhada em torno da média, dando ao gráfico um formato “achatado”. 
	- Quando o desvio-padrão é pequeno, a largura da curva é pequena, e o gráfico tem um formato mais alto e magro
- porcentagem da probabilidade total coberta em determinados intervalos medidos em quantidades de desvios-padrão em relação à média:
	- Cerca de 68,26% da probabilidade total está entre _μ-σ_ e _μ+σ._
	- Cerca de 95,44% da probabilidade total está entre _μ-2σ_ e _μ+2σ_.
	- Cerca de 99,74% da probabilidade total está entre _μ-3σ_ e _μ+3σ_

### Distribuição Normal Padrão
- A padronização da Normal é feita usando-se uma nova variável, chamada _z-score_, de tal forma que cada valor x da variável X está associado a um valor z da variável Z pela seguinte fórmula:
	- ![[zScoreDistribuicaoProbabilidadeNormal_estatisticaUVA.png]]
	- z = (x - média)/desviopadrão

# Unidade 4 - Intervalos de Confiança e Relação entre Variáveis
- Inferência Estatística 
	- estuda **como podemos interpretar dados** de que dispomos e considerarmos **se eles são representativos da população** de que foram extraídos

# Aula 1 - Intervalos de Confiança e Relação entre Variáveis
- Estimativas - valores descritivos obtidos através de estudos de amostras
- Parâmetros - valores descritivos correspondentes à população
- o valor da **média amostral X** é uma estimativa pontual da **média populacional (_μ_)**.
- o valor do **desvio-padrão amostral (S)** constitui uma estimativa do parâmetro **desvio-padrão populacional (_σ_)**
	- Sugestão de leitura - cap. 9 - [WALPOLE. Ronald, Probabilidade & Estatística: para engenharia e ciências - 8ª edição](https://plataforma.bvirtual.com.br/Acervo/Publicacao/449)
> **Nível de confiança** é a probabilidade de que o intervalo estimado contenha o parâmetro populacional, ou seja, quando definirmos um intervalo de confiança, poderemos afirmar, com uma probabilidade igual à do nível de confiança, que esse intervalo contém o parâmetro que queremos encontrar
> três os níveis de confiança sobre os quais, comumente, trabalhamos: 90%, 95% e 99%
- Atenção: intervalo de confiança de 95% **não significa** que 95% dos dados da amostra estejam dentro do intervalo
- ![[TamanhoAmostraXTabelaDistribuicaoAUsar_estatistica_UVA.png]]

# AVA 2
- ![[AVA2 Estatistica José Eduardo Alves de Carvalho.pdf]]
- ![[ConfirmacaoEnvioAVA2EstatisticaUVA.png]]