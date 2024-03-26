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

# Modo Normal
for numero in range(1, 201):
    if not numero % 2:
        print(numero)

# List Comprehension
numeros_pares = [n for n in range(1, 201) if not n % 2]
print(numeros_pares)
