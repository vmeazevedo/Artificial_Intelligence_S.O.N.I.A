# Inteligência_Artificial_S.O.N.I.A
A inteligência artificial foi desenvolvida para ser uma assistente pessoal, realizando buscas no Google e Youtube por comandos de voz.
  
## Requirements
* Será necessário instalar a biblioteca abaixo:
- pip install SpeechRecognition
- pip install DateTime
- pip install pywhatkit
- pip install gTTS
- pip install requests-html
- pip install playsound


## Exemplo de funcionamento do código:
- Ao iniciar a I.A ela automaticamente irá lhe apresentar a previsão do tempo de sua localidade na hora exata.

- Em sequência, ela irá solicitar para que o usuário se apresente.
- Quando o usuário informa o seu nome a I.A automaticamente processa o audio e o transforma em string, em sequência ela confere se o usuário já está cadastrado em sua base de dados.
- Caso o usuário não esteja cadastrado, ela realiza o cadastro do nome do usuário e solicita a ele realiar o login novamente para conceder acesso as funcionalidades.
- Caso o usuário já esteja cadastrado na base de dados, ela retorna o nome do usuário com uma saudação.
- Com o usuário devidamente logado, a I.A passa para modo de escuta, onde ela irá aguardar até que o comando de voz seja reconhecido. Em suas funcionalidades básicas, ela contém três comandos de voz: Google, Pesquisar e Desligar.

Teste da inicialização do sistema + desligamento do sistema:
https://twitter.com/vmeazevedo/status/1293375823496515591?s=09


## Comandos de Voz:
### Google
- Ao informar o comando de voz "Google" a I.A irá retornar uma frase dizendo: "O que gostaria?"
- O usuário irá dizer o conteúdo da busca no Google e a I.A irá apresentar a busca realizada.


### YouTube
- Ao informar o comando de voz "Pesquisar" a I.A irá retornar uma frase dizendo: "O que gostaria?"
- O usuário irá dizer o conteúdo da busca no Youtube e a I.A irá abrir o video desejado.

Teste do comando Google e Pesquisar:
https://twitter.com/vmeazevedo/status/1292846133807636488?s=09