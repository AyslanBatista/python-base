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
import logging
import sys

log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}

print("{:-^50}".format("Alarme De Temperatura"))

for key in info.keys():
    try:
        info[key] = float(input(f"Qual a {key} atual? ").strip())
    except ValueError:
        log.error(f"[Error] {key.capitalize()} inválida") 
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("ALERTA!!! perigo calor extremo")
elif (temp * 3) >= umidade:
    print("ALERTA!!! Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp <= 10:
    print("Frio")
else:
    print("ALERTA!!! Frio extremo")

print("#" * 50)
sys.exit(0)
