#!/usr/bin/env python3

"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2)
"""

# Solid - Single Responsibility - A função deve resolver apenas um problema
# Toda função tem um retorno, caso não seja informado um return, retorno será None


def f(x):  # assinatura
    result = 5 * (x / 2)
    return result


def double(x):
    return x * 2


valor = double(f(10))
print(valor)
print(valor == 50)


def print_in_upper(text):
    print(text.upper())


print_in_upper("bruno")


def heron(a, b, c):
    """Calcula a area de um triangulo

    Args:
        a (numero): valor1
        b (numero): valor2
        c (numero): valor3

    Returns:
        numero: valor da area de um triangulo
    """
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** 0.5 # math.sqrt(area)

def heron2(params):
    return heron(*params)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37)
]

#Map, aplique a função heron2 para cada elemento de triangulos
print(list(map(heron2, triangulos)))

for t in triangulos:
    area = heron(*t) # Desempacotar os valores de uma tupla
    print(f"A area do tringulo é: {area}")
    


