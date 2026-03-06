---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:10.447021+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: lista_de_oracao_pessoal
    weight: 8
    confidence: 0.9
  - name: reflexao_biblica_marcos_12
    weight: 9
    confidence: 0.95
  - name: analise_meditacao_ia
    weight: 7
    confidence: 0.85
  - name: questionamentos_existenciais_dia
    weight: 8
    confidence: 0.9
  - name: atividade_fisica_motivacional
    weight: 6
    confidence: 0.7
  - name: documentos_atualizados_pessoais
    weight: 5
    confidence: 0.6
  - name: tarefas_pessoais_pendentes
    weight: 7
    confidence: 0.8
  - name: trabalho_serpro_documentos
    weight: 8
    confidence: 0.9
  - name: tarefas_serpro_pendentes
    weight: 8
    confidence: 0.9
  - name: reflexao_sobre_proximo
    weight: 9
    confidence: 0.92
  cdu_primary: '200'
  cdu_secondary:
  - '230'
  - '248'
  - '370'
  cdu_description: Religião, Teologia, Ética, Educação
---
# Pessoal
## Orar [[Lista de oração]]
- Spartaco e salvação
- Baba, Dinda e salvação 
- Ana
- Roberto
- Nana e tratamento de câncer
- Antonio Carlos
- Bella e Carol
- Bubu e Juliana
- Meus pais, irmãs, cunhados, sobrinhos e sobrinhas
- Dona Vera e mudança
- Tadeu, Duda, Miguel, Maite e Cadu 
- Pelo meu dia de trabalho, pelas pessoas que trabalham comigo.



## Bíblia
- O credo de Jesus: 
> [!important]
> [[Marcos 12]]: 29-31 Jesus respondeu: “O mandamento mais importante é este: ‘Ouça, ó Israel! O Senhor, nosso Deus, é o único Senhor. 30 Ame o Senhor, seu Deus, de todo o seu coração, de toda a sua alma, de toda a sua mente e de todas as suas forças’. 31 O segundo é igualmente importante: ‘Ame o seu próximo como a si mesmo’. Nenhum outro mandamento é maior que esses”.
> [[Marcos 12 - intimo dinheiro tempo esperanca emocoes inteligencia  - tudo isso deve amar a Deus]]
- [[prompt analise meditacao e sermao]]

#### analise do chatgpt sobre minhas meditacoes em XXX


#### analise do groq sobre minhas meditacoes em marcos XXX

#### analise do deepseek sobre minhas meditacoes em marcos XXX



## Pensamentos


## Perguntas!
### No começo do dia
#### Se esse fosse o meu último dia de vida, eu iria querer fazer, hoje, as coisas que já havia planejado? 
####  O que eu posso fazer hoje para expressar o que eu tenho de mais especial e único? 
#### O que me dá certo medo, mas que eu poderia fazer hoje? 

### No fim do dia
####  Qual foi a coisa mais importante que eu fiz hoje? 
####  Eu fiz alguém sorrir hoje?
####  O que me deu mais alegria hoje? 
####  Qual foi a maior causa de conflito e estresse, hoje? 
####  O que eu aprendi hoje

## Atividade física
- https://x.com/RealScarzz/status/1924228484043264486

## Documentos atualizados no dia
```dataview
TABLE file.mtime FROM -"99 TRABALHO E GESTAO/Serpro2021" 
WHERE file.mtime >=  date("{{date}}") and file.mtime < (date("{{date}}") + dur(1 day))
SORT file.mtime asc
```

## Tarefas Pessoais do dia
```tasks
not done
due before 2024-05-06
path does not include Serpro2021
```

# Profissional
## Trabalho Serpro no dia
```dataview
TABLE file.mtime FROM "99 TRABALHO E GESTAO/Serpro2021"
WHERE file.mtime >= date("{{date}}") and file.mtime < (date("{{date}}") + dur(1 day)) 
SORT file.mtime asc
```


## Tarefas Serpro do dia
```tasks
not done
short mode
path includes Serpro2021
```
