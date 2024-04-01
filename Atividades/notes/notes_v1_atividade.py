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

arguments = sys.argv[1:]
path = os.curdir
filepath = os.path.join(path, "notes.txt")

if not arguments:
    print("Please enter the writing `new` or reading `read`")
    sys.exit(1)

argument = arguments[0].lower()

if argument == "new":
    tag = input("tag: ")
    text = input("text: ")
    titulo = arguments[1]
    with open(file=filepath, mode="a") as file_:
        file_.write(f"{titulo};{tag};{text}\n")

elif argument == "read":
    argument_tag = arguments[1].lstrip("-")
    tag = argument_tag[4:]
    print(tag)

    for line in open(file=filepath):
        read_titulo, read_tag, read_text = line.split(";")
        if tag == read_tag.strip():
            print(f"titulo:{read_titulo}\ntag: {read_tag}\ntext: {read_text}")
