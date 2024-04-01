#!/usr/bin/env python3
"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de
umidade do ar, sendo que cada caso será exibida uma mensagem de alerta dependo
das condições:

temp maior 45: ALERTA!!! perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp <0: ALERTA!!! Frio extremo
"""

while True:

    try:
        print("{:#^50}".format(" Alarme de Temperatura⏱  "))
        temp = float(input("Informe qual a temperatura atual: ").strip())
        umidade = float(input("Informe o indice de umidade do ar: ").strip())
    except ValueError as e:
        print(str(e))
        print(
            "[ERROR]Por favor informe temperatura e umidade corretamente !!!\n"
        )
        continue

    if temp > 45:
        print("ALERTA !!! perigo calor extremo 🥵🔥")
    elif (temp * 3) >= umidade:
        print("ALERTA!!! Perigo de calor úmido 🔥💦")
    elif temp >= 10 and temp <= 30:
        print("Temperatura Normal 😎🌄")
    elif temp >= 0 and temp < 10:
        print("Temperatura Frio ❄⛄")
    else:
        print("ALERTA!!! Frio extremo 🥶☃")

    if input(
        "\nAperte enter para fazer outra consulta,"
        "ou aperte qualter tecla para sair do programa"
    ):
        break
