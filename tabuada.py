#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10

Tabuada do: 1
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
...
----------------
Tabuada do: 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...
----------------
"""
__version__ = "0.1.0"
__author__ = "Ayslan"
__license__ = "Unlicense"

# numeros = [1,2,3,4,5,6,7,8,9,10]
# Transformando uma range em uma lista, range("inicio", "termino")
numeros = list(range(1,11))

# Iterable (percorriveis)

# para cada numero em numeros:
for numero in numeros:
    print(f"Tabuada do: {numero}")
    for outro_numero in numeros:
        print(f"{numero} x {outro_numero} = {numero * outro_numero}")
    print("-" * 25)
