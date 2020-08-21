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

# CONFIGURAÇÕES MIC
sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshold = 5000

def intro():
    # Função de inicialização do sistema
	msg = "S.O.N.I.A - by: Vinicius Azevedo"
	print("-" * len(msg) +  "\n{}\n".format(msg)  +   "-" * len(msg))

def previsao(local=''):
    session = HTMLSession()

    url = 'https://www.google.com.br/search?q=previsao+do+tempo&oq=previsao+do+tempo&ie=UTF-8'
    r = session.get(url)

    selector_state = '#wob_dc'
    state = r.html.find(selector_state, first=True).text
    selector_temp = '#wob_tm'
    temp = r.html.find(selector_temp, first=True).text
    return("%s°C (%s)" %(temp, state))

local = 'São Paulo'
if len(sys.argv)>0:
    sys.argv.pop(0)
    local = ' '.join(sys.argv)


def cadastro_login():
    with sr.Microphone() as source:
        cria_audio("Informe seu usuário.")
        print("Estou te ouvindo: ")
        r.adjust_for_ambient_noise(source)
        user_name = r.listen(source)
        texto = r.recognize_google(user_name,language='pt-br')

        try:    
            with open('usuarios.txt') as f:
                found = False
                for line in f:
                    if texto in line: 
                        cria_audio("Bem vindo de vólta" + texto)
                        found = True
                        opções()
        
            if not found:
                cria_audio('Não encontrei o seu usuário em meus registros.')
                cria_audio("Lembrarei de você no seu próximo login.")
                cria_audio("Por favor realize o login novamente.")
                with open('usuarios.txt', 'a') as f:
                    f.write(texto)
                    f.write("\n")

        except:
            print("Não entendi.")

def opções():
    while True:
        with sr.Microphone() as source:
                print("Estou te ouvindo: ")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

                try:
                    texto = r.recognize_google(audio,language='pt-br')
                    if (texto == 'Google'):
                        pesquisa_google()
                    if (texto == 'pesquisar'):
                        pesquisa_youtube()
                    if (texto == 'desligar'):
                        cria_audio("Desligando o sistema.")
                        playsound('audio\\down.mp3')
                        break
                except:
                    print("Não entendi.")
                    
                time.sleep(5)

def cria_audio(resp):
    #Funcao responsavel pela fala
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    audio_file = "voice"+date_string+".mp3"
    tts = gTTS(resp, lang='pt-br')
    tts.save(audio_file)
    playsound(audio_file)

# COMANDOS DE VOZ 
def pesquisa_google():
    #Função responsável por pesquisar no Google
    with sr.Microphone() as source:
        resp = "\nO que gostaria?"
        print("Aguardando a sua resposta...")
        cria_audio(resp)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source) 
        try:
            texto = r.recognize_google(audio,language='pt-br')
            print("Você solicitou a pesquisa: {}".format(texto))
            url='https://www.google.co.in/search?q='
            search_url=url+texto
            webbrowser.open(search_url)
        except:
            print("Não entendi.")

def pesquisa_youtube():
    #Função responsável por pesquisar no Youtube
    with sr.Microphone() as source:
        resp = "\nO que gostaria?"
        print("Aguardando a sua resposta...")
        cria_audio(resp)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        texto = r.recognize_google(audio,language='pt-br')
        print("Você solicitou a pesquisa: {}".format(texto))
        kit.playonyt(texto)

# ROTINA DO SISTEMA
intro()
cria_audio("Iniciândo o sistema. A previsão do tempo atual é: ")
cria_audio(previsao(local))
cadastro_login()