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

operacoes = ["sum", "sub", "mul", "div"]
arguments = sys.argv[1:]

if not arguments:
    operacao = input("Operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
else:
    operacao, n1, n2, *_ = arguments

# Tratamento de Erros
if n1.strip().isalpha():
    print(f"Erro: `{n1}` - Enter numbers only")
    sys.exit(1)
elif n2.strip().isalpha():
    print(f"Erro: `{n2}` - Enter numbers only")
    sys.exit(1)


if operacao.strip() == operacoes[0]:
    print(float(n1) + float(n2))
elif operacao.strip() == operacoes[1]:
    print(float(n1) - float(n2))
elif operacao.strip() == operacoes[2]:
    print(float(n1) * float(n2))
elif operacao.strip() == operacoes[3]:
    print(float(n1) / float(n2))
else:
    print(f"The reported operation was invalidated `{operacao}`")
    print("Please enter one of the following operations: sum, sub, mul, div")
    sys.exit(1)
