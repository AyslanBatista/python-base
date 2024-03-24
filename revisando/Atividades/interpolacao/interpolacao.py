#!/usr/bin/env python3
__version__ = "0.1.2"
__author__ = "Ayslan"
__license__ = "Unlicense"

import os
import sys


arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, "emails.txt")  # emails.txt
templatepath = os.path.join(path, "email_tmpl.txt")  # email_tmpl.txt

clientes = []
for line in open(file=filepath):
    name, email = line.split(",")

    # TODO substituir por envio de email
    print(f"Enviando email para: {email}")
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
    print("-" * 50)
