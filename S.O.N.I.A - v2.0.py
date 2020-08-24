# Bibliotecas
import speech_recognition as sr
import datetime
import webbrowser
import time
import pywhatkit as kit
import re
import sys
from gtts import gTTS
from playsound import playsound
from requests_html import HTMLSession
import pyttsx3
from threading import Thread

# CONFIGURAÇÕES MIC
sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshold = 5000

# Utilizando a biblioteca pyttsx3 para a criação do audio, dessa forma, não é necessário buscar por arquivos de audio

def speak(text):
    speaker = pyttsx3.init('sapi5')
    speaker.say(text)
    speaker.runAndWait()

# Criando um método para lidar apenas com o reconhecimento de voz
def Recognition():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)

            print('Say:')

            sound = recognizer.listen(source)
            speech = recognizer.recognize_google(sound, language='pt').lower()
            print('You said: ', speech)

            return speech
    except:
        return ''

def intro():
    # Função de inicialização do sistema
	msg = 'S.O.N.I.A - by: Vinicius Azevedo'
	print('-' * len(msg) +  '\n{}\n'.format(msg)  +   '-' * len(msg))

def previsao(local=''):
    session = HTMLSession()

    url = 'https://www.google.com.br/search?q=previsao+do+tempo&oq=previsao+do+tempo&ie=UTF-8'
    r = session.get(url)

    selector_state = '#wob_dc'
    state = r.html.find(selector_state, first=True).text
    selector_temp = '#wob_tm'
    temp = r.html.find(selector_temp, first=True).text
    return('%s°C (%s)' %(temp, state))

local = 'São Paulo'
if len(sys.argv)>0:
    sys.argv.pop(0)
    local = ' '.join(sys.argv)


def cadastro_login():
    speak('Informe seu usuário.')
    texto = Recognition()
   
    with open('usuarios.txt') as f:
        found = False
        for line in f:
            if texto in line: 
                speak('Bem vindo de vólta' + texto)
                found = True
                opções()
        
            if not found:
                speak('Não encontrei o seu usuário em meus registros.')
                speak('Lembrarei de você no seu próximo login.')
                speak('Por favor realize o login novamente.')
                with open('usuarios.txt', 'a') as f:
                    f.write(texto)
                    f.write('\n')

# Utilizando IN ao inves de == para que o comando seja acionado quando a palavra estiver na string, possibilitando
# o reconhecimento do comando dentro de uma frase.
# Utilizando apenas o RADICAL da palavra para a checagem, possibilitando que a palavra possa ser dita em diferentes
# forma, ex: comando: Desligar Radical: Deslig Possibilidades: desligar, desligue, desligando...

def opções():
    while True:
        texto = Recognition()
        if ('google' in texto):
            pesquisa_google()
        if ('pesquis' in texto):
            pesquisa_youtube()
        if ('deslig' in texto):
            speak('Desligando o sistema.')
            playsound('audio\\down.mp3')
            break    
        time.sleep(5)

# COMANDOS DE VOZ 
def pesquisa_google():
    #Função responsável por pesquisar no Google
    resp = '\nO que gostaria?'
    speak(resp)
    print('Aguardando a sua resposta...')
    texto = Recognition()
    print('Você solicitou a pesquisa: {}'.format(texto))
    url='https://www.google.co.in/search?q='
    search_url=url+texto
    webbrowser.open(search_url)
    
def pesquisa_youtube():
    #Função responsável por pesquisar no Youtube
    resp = '\nO que gostaria?'
    speak(resp)
    print('Aguardando a sua resposta...')
    texto = Recognition()
    print('Você solicitou a pesquisa: {}'.format(texto))
    kit.playonyt(texto)

# ROTINA DO SISTEMA
intro()
speak('Iniciando o sistema. A previsão do tempo atual é ')
speak(previsao(local))
cadastro_login()