from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def envia_Email(From, Assunto, Login, Senha, Text):
    msg = MIMEMultipart()

    Emails = open('Lista.txt', 'r')

    for linha in Emails:
        msg['to'] = linha
        msg['from'] = From
        msg['subject'] = Assunto

        mensagem = MIMEText(Text)

        msg.attach(mensagem)

        try:
            with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(Login, Senha)
                smtp.send_message(msg)
                print('Email enviado com sucesso')
        except:
            print('Houve um erro na hora de enviar os emails')


envia_Email('Teste', 'Teste', 'teste@gmail.com', 'senha', 'Esse é um email de teste')
