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
"""
__version__ = "0.1.0"
__author__ = "Ayslan"
__license__ = "Unlicense"

import sys

# Argumentos que poderão ser passados para o programa
arguments = {
    "operacoes": ["sub", "sum", "mul", "div"],
    "valores": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
}


# Validação dos dados que são passados no momento de rodar o programa,
# Caso esteja tudo OK!, ele roda o programa
if len(sys.argv) > 1:
    if len(sys.argv[1:]) != 3:
        print(f"Invalid Option `{sys.argv[4:]}`")
        sys.exit()
    elif sys.argv[1] not in arguments["operacoes"]:
        print(f"Invalid Option `{sys.argv[1]}`")
        sys.exit()
    for op in sys.argv[2].replace(".", ""):
        if op not in arguments["valores"]:
            print(f"Invalid Option `{sys.argv[2]}`")
            sys.exit()
    for op in sys.argv[3].replace(".", ""):
        if op not in arguments["valores"]:
            print(f"Invalid Option `{sys.argv[3]}`")
            sys.exit()
    else:
        if "." in sys.argv[2]:
            n1 = float(sys.argv[2])
        else:
            n1 = int(sys.argv[2])
        if "." in sys.argv[3]:
            n2 = float(sys.argv[3])
        else:
            n2 = int(sys.argv[3])

        if sys.argv[1] == "sum":
            print(f"{n1 + n2}")
            sys.exit()
        elif sys.argv[1] == "sub":
            print(f"{n1 - n2}")
            sys.exit()
        elif sys.argv[1] == "mul":
            print(f"{n1 * n2}")
            sys.exit()
        elif sys.argv[1] == "div":
            print(f"{n1 / n2}")
            sys.exit()


# Input do Usuário com Validação dos dados
operacao = input("Operação: ")
if operacao not in arguments["operacoes"]:
    print(f"Invalid Option `{operacao}`")
    sys.exit()

n1 = input("n1: ")
for n in n1.replace(".", ""):
    if n not in arguments["valores"]:
        print(f"Invalid Option `{n}`")
        sys.exit()

n2 = input("n2: ")
for n in n2.replace(".", ""):
    if n not in arguments["valores"]:
        print(f"Invalid Option `{n}`")
        sys.exit()


# Resultado
if operacao == "sum":
    print(f"{int(n1) + int(n2)}")
elif operacao == "sub":
    print(f"{int(n1) - int(n2)}")
elif operacao == "mul":
    print(f"{int(n1) * int(n2)}")
elif operacao == "div":
    print(f"{int(n1) / int(n2)}")
