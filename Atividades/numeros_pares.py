#!/usr/bin/env python3
"""
Faça um programa que impre os números pares de 1 a 200
ex
`python3 numeros_pares.py`
2
4
6
8
...
"""


# Utilizando for
for n in range(1, 201):
    if n % 2 != 0:
        continue
    print(n)

# Utilizando while
n = 0
while n < 201:
    if n % 2 != 0:
        n += 1
        continue
    print(n)
    n += 1
