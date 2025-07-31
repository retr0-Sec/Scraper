import requests
import re
import sys
import smtplib
import os
from email.message import EmailMessage
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

def Validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(padrao, email) is not None

def Scraper():
    texto = []
    headers = {"User-Agent": "Mozilla/5.0"}
    endpoint = "https://www.cnnbrasil.com.br/tudo-sobre/hacker/"
    response = requests.get(endpoint, headers=headers)
    puxe = BeautifulSoup(response.text, "lxml")
    noticia = puxe.find_all("h2")
    for resultado in noticia:
        texto.append(resultado.text)
    return texto

erros = 0
print("=== COLETA NEWS SEC ===")
name = input("Como voçê se chama? ").strip()
print(f"Certo, Olá {name} espero que esteja bem, antes de executar o meu serviço preciso que voçê informe o seu Email!")
while erros < 3:
    email = input("Insira seu email: ").strip()
    if Validar_email(email):
        print("Email Correto, logo Enviaremos o conteúdo!!")
        print("ATENTE- SE!!! caso o email não esteja em seu controle, voçê não receberá o conteudo")
        break
    else:
        print("Email incorreto!! Verifique se está correto e tente novamente")
        erros += 1
        if erros == 3:
            print("Tentativas esgotadas!!!, reinicie o script")

print("\nAVISO!!!! ESSE SCRIPT É PARA CUNHO INFORMATIVO, NÃO ME RESPOSABILIZO PELO MAU USO.")
per1 = input("Esse email é seu? Voçê está informado que é por sua responsabilidade esse email? yes/no: ").lower()
if per1 == "yes":
    print("continuando...")

if per1 != "yes":
    print("atente pra digitar (yes) correto, ou o script é interrompido. (IGNORE Caso a resposta foi não ")
    sys.exit()


#preparo e envio dos emails

def enviar_Email(email_destino):
    email_remetente = os.getenv("email_remetente")
    senha = os.getenv("senha_app")

    conteudo = "ULTIMAS NOTICIAS DA CNN BRASIL:\n\n"
    web_scraping = Scraper()
    for texto in web_scraping:
        conteudo += (f"[+] {texto}\n\n")
    conteudo += (f"https://www.cnnbrasil.com.br/tudo-sobre/hacker/")
    conteudo += (f"confira com mais detalhes em ↑\n")
    conteudo+= (f"EMAIL ENVIADO A PEDIDO DE: {name.upper()}")


    mensagem_enviada = EmailMessage()
    mensagem_enviada["From"] = email_remetente
    mensagem_enviada["To"] = email_destino
    mensagem_enviada["Subject"] = "ULTIMAS NOTICIAS DE HACKERS/SEGURANÇA DIGITAL DA CNN BRASIL!!!!"
    mensagem_enviada.set_content(conteudo)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_remetente, senha)
        smtp.send_message(mensagem_enviada)
        print("Email enviado com sucesso [+]")

enviar_Email(email)
