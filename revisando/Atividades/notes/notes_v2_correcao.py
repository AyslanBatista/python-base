#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text:
Anotacao geral sobre carreira de tecnologia

$ notes.py read tech
"""

__version__ = "0.3.0"
__author__ = "Ayslan"
__license__ = "Unlicense"

import logging
import os
import sys
from logging import handlers

# CONFIGURAÇÂO DO LOG
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("ayslan", log_level)
fh = handlers.RotatingFileHandler(
    "historico.log",
    maxBytes=10**6,
    backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s"
)
fh.setFormatter(fmt)
log.addHandler(fh)


path = os.curdir
filepath = os.path.join(path, "notes.txt")
cmds = ("read", "new")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"you must specify subcommand: {cmds}")
    sys.exit(1)


if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")


while True:

    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag?: ").strip().lower()

        # leitura das notas
        for line in open(file=filepath):
            title, tag, text = line.split("\t")
            if tag == arg_tag:
                print(f"title: {title}")
                print(f"text: {text}")
                print("-" * 30)

    if arguments[0] == "new":
        try:
            title = arguments[1]

        except IndexError:
            title = input("Qual é o titulo?: ").strip().title()

        text = [
            f"{title}\n",
            input("tag: ").strip(),
            input("text:\n").strip(),
        ]

        try:
            with open(filepath, "a") as file_:
                file_.write("\t".join(text) + "\n")
        except PermissionError as e:
            log.error("%s", str(e))
            print(str(e))
            sys.exit(1)

    cont = input(f"Quer continuar {arguments[0]} notas? [N/y]").strip().lower()
    if cont != "y":
        break
