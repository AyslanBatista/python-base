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
from types import NoneType

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

if info["temperatura"] > 45:
    print("ALERTA!!! perigo calor extremo")
elif (info["temperatura"] * 3) >= info["umidade"]:
    print("ALERTA!!! Perigo de calor úmido")
elif info["temperatura"] >= 10 and info["temperatura"] <= 30:
    print("Normal")
elif info["temperatura"] >= 0 and info["temperatura"] <= 10:
    print("Frio")
else:
    print("ALERTA!!! Frio extremo")

print("#" * 50)
sys.exit(0)
