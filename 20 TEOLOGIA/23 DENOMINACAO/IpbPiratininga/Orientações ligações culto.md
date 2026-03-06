---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:41:21.494455+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: configuracao_rede_computador
    weight: 9
    confidence: 0.98
  - name: instalacao_equipamento_audio
    weight: 8
    confidence: 0.95
  - name: conexao_cabo_rede
    weight: 7
    confidence: 0.97
  - name: conexao_eletrica_equipamentos
    weight: 7
    confidence: 0.96
  - name: configuracao_roteador_wifi
    weight: 6
    confidence: 0.94
  - name: configuracao_placa_som
    weight: 8
    confidence: 0.93
  - name: configuracao_microfone_sem_fio
    weight: 7
    confidence: 0.92
  - name: configuracao_transmissao_ao_vivo
    weight: 10
    confidence: 0.99
  - name: uso_software_reaper
    weight: 9
    confidence: 0.96
  - name: uso_software_obs_studio
    weight: 9
    confidence: 0.97
  cdu_primary: '004.7'
  cdu_secondary:
  - '621.39'
  - '681.3'
  - '781.6'
  cdu_description: 004.7 Redes de computadores; 621.39 Telecomunicações; 681.3 Processamento de dados. Computadores; 781.6 Instrumentos musicais. Execução musical.
---
[[Missão iPB Piratininga]]
Temos 2 grandes "grupos" de setup a realizar: Conexões e setups no computador para transmissão

1 - Conexões

a) Conexão do cabo de rede - levar pela janela lateral até a secretaria e ligar a ponta do cabo de rede (azul) que tem uma marcação com adesivo no roteador que fica em cima do armário

b) Conexões elétricas - Ligar o estabilizador na tomada dentro da salinha; Ligar nele a extensão preta que "roda" e levar o cabo até o portãozinho, onde está chegando o cabo de rede; Ligar as duas "réguas" de tomadas no estabilizador; Ligar o amplificador em uma das réguas

c) Ligação do roteador wifi - Ligar ele na extensão e conectar o cabo de rede na entrada "wan"

d) Conexões de cabos de som - Ligar a placa de som na tomada de uma das réguas; Ligar o receptor do microfone sem fio (Shure) em uma das tomadas das réguas; Conectar o menor cabo de microfone entre o receptor do microfone e o canal 1 da placa de som; Ligar o receptor do transmissor (verde, plug "banana") sem fio do violão no canal 2 da placa de som; Ligar um cabo de microfone para o microfone do 2o vocal no canal 3 da placa; Conectar um cabo "banana" na saída de headphone da placa e a outra ponta na entrada 1 da caixa amplificada

e) Conexões no computador - Ligar o projetor em uma das tomadas das réguas; conectar o cabo "VGA" no projetor e a outra ponta na entrada HDMI do computador; Montar a câmera e ligar o cabo USB dele em um dos conectores do computador; Colocar o cabo USB na placa de som e a outra ponta em um dos conectores do computador

2 - Setup do computador

a) Ligar o computador - senha "igreja". Ele já deve conectar automaticamente na rede wifi criada pelo nosso roteador

b) Abrir o arquivo com louvores ou baixar da internet e abrir. Com o mouse levar ele até a "tela" do projetor e teclar, ao mesmo tempo, "fn" e F11 (é o comando para ampliar o arquivo em toda a tela do projetor)

c) Teclar no botão de "comando" do teclado (é aquele que tem um símbolo do Windows). Esse botão vai abrir uma caixa para digitar um texto e pesquisar um aplicativo. 

d) Digitar "reaper" e dar enter. Vai abrir o software que recebe o som da placa, coloca alguns efeitos e o envia tanto para o amplificador (nosso som "local") quanto para o OBS (o software que controla a transmissão e nosso som "externo"). Três faixas vão aparecer. Cada uma delas correspondendo a um canal da placa. Assim,a faixa 1 é o canal 1 (microfone sem fio), a faixa 2 é o canal 2 (violão) e faixa 3 o canal 3 (segundo microfone). Todas as faixas precisam estar "armadas" para receber e transmitir o som. É o 1o botão, vermelho, em cada faixa.

e) Testar a entrada do som - em cada microfone e instrumento tocar e falar e verificar se o "meter" de entrada está se mexendo. 

f) Teclar novamente no botão de "comando" do teclado (é aquele que tem um símbolo do Windows). Esse botão vai abrir uma caixa para digitar um texto e pesquisar um aplicativo.

g) Digitar "OBS" e dar enter. Vai abrir o OBS Studio, com as cenas já configuradas para a transmissão. São 3 cenas - abertura, louvor e amplo. 

h) Se tudo correr bem, ao falar em um microfone você verá o "meter" de entrada de som do OBS se movimentar, como acontece no Reaper. Se não se movimentar, clicar no botão de 



