---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:52.991272+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: seguranca_marketplace
    weight: 9
    confidence: 0.9
  - name: certificado_digital_gov_br
    weight: 8
    confidence: 0.85
  - name: autorizacao_cnpj_cpf
    weight: 7
    confidence: 0.75
  - name: autenticacao_dois_fatores_gov_br
    weight: 8
    confidence: 0.8
  - name: credenciais_gov_br_empresas
    weight: 9
    confidence: 0.88
  - name: falha_inscricao_mei
    weight: 10
    confidence: 0.95
  - name: api_backend_acesso_externo
    weight: 9
    confidence: 0.92
  - name: venda_inscricao_mei
    weight: 7
    confidence: 0.7
  - name: seguranca_acesso_frontend_mei
    weight: 8
    confidence: 0.82
  - name: reuniao_seat_mei
    weight: 6
    confidence: 0.65
  cdu_primary: '347.73'
  cdu_secondary:
  - 004.032.1
  - '351.71'
  cdu_description: Direito comercial e direito empresarial. Direito de registro de empresas. Segurança da informação e proteção de dados. Serviços públicos digitais.
---
#### 20210516 - URC, SUPSI, SUPDR, SEDAT - Segurança da solução Marketplace
- Não garanto que o Marketplace recebeu autorização minha para abrir um CNPJ para meu CPF
- gov.br entrega um certificado digital válido emitido pelo ITI
- Usar os critério do próprio gov.br para obtenção desse certificado (ser conta prata ou ouro) e um two fase authenticator no acesso gov.br
- 

#### Equipe MEI 20210203
- Cadu explicando o problema
- Galuzo: Empresas pedem as credenciais do gov.br
- Captcha, email, token "SSR"

#### Cadu 20210201
- Falha na inscriação no MEI
	- API do backend pode ser chamado de qq cliente. Empresas estão vendendo a inscrição e chamado o backend direto
	- Equipe entende que não consegue garantir que somente o frontend MEI acesse.
- Cadu agendou reunião com SEAT& para 20210203