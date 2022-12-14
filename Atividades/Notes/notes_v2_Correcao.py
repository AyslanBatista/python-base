#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text:
Anotacao geral sobre carreira de tecnologia

$ notes.py read tech
"""

__version__ = "0.1.0"
__author__ = "Ayslan"
__license__ = "Unlicense"


import os
import sys

# Diretorio atual
path = os.curdir
filepath = os.path.join(path, "notes.txt")

# Variaveis
arguments = sys.argv[1:]
cmds = ("read", "new")

# Validações
if not arguments:
    print("Invalid usage")
    print(f"you must specity subcommand {cmds}")
    sys.exit(1)

elif arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

elif len(arguments) > 2:
    print(f"Invalid usage `{sys.argv[3:]}`")
    sys.exit(1)

while True:

    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag: ").strip().lower()

        # Leitura das notas
        for line in open(filepath):
            title, tag, text = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"title: {title}")
                print(f"text: {text}")
                print("-" * 30)
                print()

    if arguments[0] == "new":
        # Criacao da nota
        try:
            title = arguments[1]
        except IndexError:
            title = input("Qual é o titulo: ").strip().title()
        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]
        # \t - tsv
        with open(filepath, "a") as file_:
            # Criando uma lista de string separado pelo \t
            file_.write("\t".join(text) + "\n")

    if len(arguments) > 1:
        arguments.remove(arguments[1])
    cont = input(f"Quer continuar {arguments[0]} notas? [n/y]").strip().lower()
    if cont != "y":
        break
