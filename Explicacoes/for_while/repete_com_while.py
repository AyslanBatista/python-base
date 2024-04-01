#!/usr/bin/env python3

# While - Enquanto - Precisa ter uma condição

n = 0
while n < 101:  # Condicao de parada
    if n == 40:
        break  # Condicao de parada
    print(n)
    n += 1

n = 0
while n < 101:  # Condicao de parada
    if n == 40 and n <= 60:  # Intervalo entre dois numeros

        # Incremento para não cair em um deadlock
        # Travado pois a condição n, não aumentou de valor
        n += 1
        continue  # pula
    print(n)
    n += 1

n = 0
while n < 101:  # Condicao de parada
    if n % 2 != 0:  # pular os numeros impares
        n += 1
        continue
    print(n)
    n += 1
