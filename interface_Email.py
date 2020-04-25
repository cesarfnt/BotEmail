#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.1
#  in conjunction with Tcl version 8.6
#    Apr 25, 2020 03:38:43 PM -03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from tkinter import *
from tkinter import filedialog
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

file_path = ""


def envia_email():
    if not file_path == '':
        Emails = open(file_path, 'r')

    for linha in Emails:
        msg = MIMEMultipart()

        msg['to'] = linha
        msg['from'] = Entry1.get()
        msg['subject'] = Entry1_5.get()

        mensagem = MIMEText(Entry1_6.get())

        msg.attach(mensagem)

        try:
            with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(Entry1_3.get(), Entry1_4.get())
                smtp.send_message(msg)
                print('Email enviado com sucesso')
        except:
            print('Houve um erro na hora de enviar os emails')

def pegar_arquivo():
    global file_path
    file_path = filedialog.askopenfilename()

top = tk.Tk()

'''This class configures and populates the toplevel window.
   top is the toplevel containing window.'''
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
font9 = "-family {SimSun} -size 20"
style = ttk.Style()
if sys.platform == "win32":
    style.theme_use('winnative')
style.configure('.',background=_bgcolor)
style.configure('.',foreground=_fgcolor)
style.configure('.',font="TkDefaultFont")
style.map('.',background=
    [('selected', _compcolor), ('active',_ana2color)])

top.geometry("877x1091+1534+525")
top.minsize(232, 1)
top.maxsize(11368, 2119)
top.resizable(1, 1)
top.title("Envio Automatico")
top.configure(background="#d9d9d9")

Label1 = tk.Label(top)
Label1.place(relx=0.08, rely=0.026, height=69, width=123)
Label1.configure(background="#d9d9d9")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(font=font9)
Label1.configure(foreground="#000000")
Label1.configure(text='''Nome''')

Entry1 = tk.Entry(top)
Entry1.place(relx=0.08, rely=0.105,height=34, relwidth=0.597)
Entry1.configure(background="white")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="TkFixedFont")
Entry1.configure(foreground="#000000")
Entry1.configure(insertbackground="black")

Label1_1 = tk.Label(top)
Label1_1.place(relx=0.08, rely=0.137, height=69, width=133)
Label1_1.configure(activebackground="#f9f9f9")
Label1_1.configure(activeforeground="black")
Label1_1.configure(background="#d9d9d9")
Label1_1.configure(disabledforeground="#a3a3a3")
Label1_1.configure(font="-family {SimSun} -size 20")
Label1_1.configure(foreground="#000000")
Label1_1.configure(highlightbackground="#d9d9d9")
Label1_1.configure(highlightcolor="black")
Label1_1.configure(text='''Email''')

Entry1_3 = tk.Entry(top)
Entry1_3.place(relx=0.08, rely=0.202,height=34, relwidth=0.597)
Entry1_3.configure(background="white")
Entry1_3.configure(disabledforeground="#a3a3a3")
Entry1_3.configure(font="TkFixedFont")
Entry1_3.configure(foreground="#000000")
Entry1_3.configure(highlightbackground="#d9d9d9")
Entry1_3.configure(highlightcolor="black")
Entry1_3.configure(insertbackground="black")
Entry1_3.configure(selectbackground="#c4c4c4")
Entry1_3.configure(selectforeground="black")

Label1_2 = tk.Label(top)
Label1_2.place(relx=0.08, rely=0.238, height=67, width=133)
Label1_2.configure(activebackground="#f9f9f9")
Label1_2.configure(activeforeground="black")
Label1_2.configure(background="#d9d9d9")
Label1_2.configure(disabledforeground="#a3a3a3")
Label1_2.configure(font="-family {SimSun} -size 20")
Label1_2.configure(foreground="#000000")
Label1_2.configure(highlightbackground="#d9d9d9")
Label1_2.configure(highlightcolor="black")
Label1_2.configure(text='''Senha''')

Entry1_4 = tk.Entry(top, show='*')
Entry1_4.place(relx=0.08, rely=0.302,height=34, relwidth=0.597)
Entry1_4.configure(background="white")
Entry1_4.configure(disabledforeground="#a3a3a3")
Entry1_4.configure(font="TkFixedFont")
Entry1_4.configure(foreground="#000000")
Entry1_4.configure(highlightbackground="#d9d9d9")
Entry1_4.configure(highlightcolor="black")
Entry1_4.configure(insertbackground="black")
Entry1_4.configure(selectbackground="#c4c4c4")
Entry1_4.configure(selectforeground="black")

Label1_3 = tk.Label(top)
Label1_3.place(relx=0.08, rely=0.339, height=67, width=195)
Label1_3.configure(activebackground="#f9f9f9")
Label1_3.configure(activeforeground="black")
Label1_3.configure(background="#d9d9d9")
Label1_3.configure(disabledforeground="#a3a3a3")
Label1_3.configure(font="-family {SimSun} -size 20")
Label1_3.configure(foreground="#000000")
Label1_3.configure(highlightbackground="#d9d9d9")
Label1_3.configure(highlightcolor="black")
Label1_3.configure(text='''Assunto''')

Entry1_5 = tk.Entry(top)
Entry1_5.place(relx=0.08, rely=0.403,height=34, relwidth=0.597)
Entry1_5.configure(background="white")
Entry1_5.configure(disabledforeground="#a3a3a3")
Entry1_5.configure(font="TkFixedFont")
Entry1_5.configure(foreground="#000000")
Entry1_5.configure(highlightbackground="#d9d9d9")
Entry1_5.configure(highlightcolor="black")
Entry1_5.configure(insertbackground="black")
Entry1_5.configure(selectbackground="#c4c4c4")
Entry1_5.configure(selectforeground="black")

Label1_4 = tk.Label(top)
Label1_4.place(relx=0.068, rely=0.431, height=66, width=165)
Label1_4.configure(activebackground="#f9f9f9")
Label1_4.configure(activeforeground="black")
Label1_4.configure(background="#d9d9d9")
Label1_4.configure(disabledforeground="#a3a3a3")
Label1_4.configure(font="-family {SimSun} -size 20")
Label1_4.configure(foreground="#000000")
Label1_4.configure(highlightbackground="#d9d9d9")
Label1_4.configure(highlightcolor="black")
Label1_4.configure(text='''Texto''')

Entry1_6 = tk.Entry(top)
Entry1_6.place(relx=0.08, rely=0.495,height=174, relwidth=0.597)
Entry1_6.configure(background="white")
Entry1_6.configure(disabledforeground="#a3a3a3")
Entry1_6.configure(font="TkFixedFont")
Entry1_6.configure(foreground="#000000")
Entry1_6.configure(highlightbackground="#d9d9d9")
Entry1_6.configure(highlightcolor="black")
Entry1_6.configure(insertbackground="black")
Entry1_6.configure(selectbackground="#c4c4c4")
Entry1_6.configure(selectforeground="black")

TSeparator1 = ttk.Separator(top)
TSeparator1.place(relx=0.091, rely=0.724, relwidth=0.798)

Button1 = tk.Button(top, command=pegar_arquivo)
Button1.place(relx=0.125, rely=0.761, height=84, width=152)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#d9d9d9")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''Abrir arquivo''')

Button1_7 = tk.Button(top, command=envia_email)
Button1_7.place(relx=0.536, rely=0.761, height=84, width=152)
Button1_7.configure(activebackground="#ececec")
Button1_7.configure(activeforeground="#000000")
Button1_7.configure(background="#555efb")
Button1_7.configure(disabledforeground="#a3a3a3")
Button1_7.configure(foreground="#ffffff")
Button1_7.configure(highlightbackground="#d9d9d9")
Button1_7.configure(highlightcolor="black")
Button1_7.configure(pady="0")
Button1_7.configure(relief="flat")
Button1_7.configure(text='''Enviar''')
top.mainloop()
