---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:58.882591+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: instalacao_token_safenet_5110
    weight: 10
    confidence: 0.98
  - name: configuracao_google_chrome
    weight: 9
    confidence: 0.95
  - name: configuracao_chromium
    weight: 9
    confidence: 0.95
  - name: sistema_operacional_ubuntu_2004
    weight: 8
    confidence: 0.9
  - name: gerenciamento_biblioteca_nss3_tools
    weight: 7
    confidence: 0.85
  - name: uso_terminal_linux
    weight: 7
    confidence: 0.88
  - name: comando_sudo_apt_install
    weight: 6
    confidence: 0.8
  - name: comando_modutil
    weight: 8
    confidence: 0.92
  - name: adicao_modulo_seguranca_token
    weight: 9
    confidence: 0.93
  - name: verificacao_instalacao_token
    weight: 7
    confidence: 0.87
  cdu_primary: '004.6'
  cdu_secondary:
  - '004.4'
  - '004.7'
  cdu_description: Redes de computadores. Sistemas de comunicação de dados. Segurança de redes. Instalação e configuração de hardware de segurança (tokens) em sistemas operacionais e navegadores.
---
(https://chat.[[serpro]].gov.br/channel/teletrabalho-problemas?msg=B7DBR7rwmmWRd4YS5)

Usando Token SafeNet 5110 no Google Chrome ou Chromium (Ubuntu 20.04)

1. ABRA O TERMINAL E EXECUTE O COMANDO ABAIXO QUE IRÁ INSTALAR A BIBLIOTECA NO SISTEMA:
sudo apt install libnss3-tools ; mkdir -p $HOME/.pki/nssdb

2. FECHE O CHROME ANTES DE EXECUTAR O COMANDO ABAIXO. COM O TERMINAL AINDA ABERTO, EXECUTE O COMANDO ABAIXO PARA ADICIONAR O TOKEN A LISTA DE DISPOSITIVOS E MÓDULO DE SEGURANÇA:
modutil -dbdir sql:.pki/nssdb/ -add "SERPRO" -libfile /usr/lib/libeToken.so

Após a execução do comando e confirmação será exibida uma mensagem assim:
“Module “SERPRO” added to database.”

3. Para verficar se o token foi adicionado corretamente excecute o comando:
modutil -dbdir sql:.pki/nssdb/ -list

Tudo pronto. Seu token já está pronto para funcionar no Google Chrome ou Chromium.

FONTE: https://diadialinux.wordpress.com/2020/05/21/usando-token-no-google-chrome-ou-chromium/