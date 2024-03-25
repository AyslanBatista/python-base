#!/usr/bin/env python3
"""Calculadora infix.
Funcionamento:
[operação] [n1] [n2]
Operações:
sum -> +
sub -> -
mul -> *
div -> /
Uso:
$ infixcalc.py sum 5 2
7
$ infixcalc.py mul 10 5
50
$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `infixcalc.log`
"""
__version__ = "0.2.1"
__author__ = "Ayslan"
__license__ = "Unlicense"


import logging
import os
import sys
from datetime import datetime
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


arguments = sys.argv[1:]

# Validação
if not arguments:
    operation = input("Operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]


if len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # Verificando se o valor que foi passado é um numero
    # TODO: Repitição while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)

    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))

# TODO: usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado é {result}")

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

try:
    with open(file=filepath, mode="a") as file_:
        file_.write(
            f"{timestamp} - {user} {operation}, {n1}, {n2} = {result}\n"
        )
except PermissionError as e:
    log.error("%s", str(e))
    print(str(e))
    sys.exit(1)
