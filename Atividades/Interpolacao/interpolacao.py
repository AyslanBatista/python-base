#!/usr/bin/env python3
""" Template para enviar e-mail com informações de cada cliente

 Olá, Maria
    
    Tem interesse em comprar caneta?
    
    Este produto é ótimo para resolver
    Escrever muito bem
    
    Clique agora em https://canetaslegais.com
    
    Apenas 1 disponiveis!
    
    Preço promocional 50.50
"""
__version__ = "0.1.1"
__author__ = "Ayslan"
__license__ = "Unlicense"

import os
import smtplib
import sys
from email.mime.text import MIMEText  # TEMPLATE PRONTO

# Argumento na linha de comando
arguments = sys.argv[1:]

# Validação
if not arguments:
    print("informe o nome do arquivo de emails")
filename = arguments[0]
templatename = arguments[1]

# Caminho do arquivo que vai ser lido os emails
path = os.curdir
filepath = os.path.join(path, "emails.txt")
templatepath = os.path.join(path, templatename)

with smtplib.SMTP(host="localhost", port=8025) as server:

    for line in open(filepath):
        name, email = line.split(",")
        text = (
            open(templatepath).read() % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
              }
        )

        from_ = "bruno@rocha.com"
        to = ", ".join([email])
        
        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())
