#!/usr/bin/env python3
__version__ = "0.1.2"
__author__ = "Ayslan"
__license__ = "Unlicense"

import os
import smtplib
import sys
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, "emails.txt")  # emails.txt
templatepath = os.path.join(path, "email_tmpl.txt")  # email_tmpl.txt

with smtplib.SMTP(host="localhost", port=8025) as server:

    for line in open(file=filepath):
        name, email = line.split(",")

        text = open(templatepath).read() % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }

        from_ = "bruno@rocha.com"
        to = ", ".join([email])

        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())
