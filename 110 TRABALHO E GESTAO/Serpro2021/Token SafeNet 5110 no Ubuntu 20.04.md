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