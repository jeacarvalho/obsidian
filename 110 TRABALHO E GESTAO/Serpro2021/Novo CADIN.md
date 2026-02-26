## 20230531 - Api gateway novo Cadin
- Requisitos 
	- Ser utilizado por entidades públicas e privadas  
	- Alta disponibilidade: 99,9% com 1000 requisições em 1 segundo  
	- Mecanismo de gestão da API (cadastro de entidades que vão usar, geração de token, bilhetagem, etc) que possa ser operado pela própria PGFN  
	- Monitoração  
	- Logs
- 
___
## 202200928 - Novo CADIN X Plin
- ConectaGOV - Plin para governo, controlado pela SGD
- Plin não pode ser usado por entes externos
	- Mas Bisotto só não faz pq não tem recurso para isso.

___
## 202200810 - Apoio Arquitetural - Novo CADIN PGFN + SIRA
- Cadin - cad. inadimplentes, gerido pelo BC. Uma lei transfere para a PGFN. 
- PGFN quer fazer novo sistema
- 22 a 26/08 inception em Brasília
- Grande base adabas com 110 milhões de registros, que devem ser migrados para nova solução
- Solução nova vai englobar essa base, api que permita que consultar, inserir e excluir do Cadin. 
- Uma app web para gestão da PGFN
- Manter mecanismo que existe de troca de arquivos
- Principal cliente do Cadin é Caixa econômica
- Stamato líder conduzindo.
### SIRA
- Grande datalake cujos dados serão servidos a entes públicos e privados
- Time SUPAI estava presente (Osnir)
- Armazenamento dos dados foi bem discutido