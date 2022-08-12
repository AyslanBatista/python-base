#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text:
Anotacao geral sobre carreira de tecnologia

$ notes.py read --tag=tech
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
keys = "tag"

# Validações
if not arguments:
    print("Invalid usage")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    # Leitura das notas

    # Tratamento da informação
    key, value = arguments[1].split("=")
    key = key.lstrip("-").strip()

    # Validação dos argumentos que foram passados
    if key not in keys:
        print(f"Invalid Option `{key}`")
        sys.exit()

    # Buscando a chave key e printando o valor text
    print(open(filepath).read())
    for line in filepath:
        print(line)


if arguments[0] == "new":
    # Criacao da nota
    title = arguments[1]
    tag = input("tag: ")
    text = input("text: \n")
    with open(filepath, "a") as note:
        note.writelines(f"titulo:{title};tag:{tag};text:{text}\n")
