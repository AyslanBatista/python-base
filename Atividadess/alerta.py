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

# TODO: Mover para módulo de utilidades

def is_completely_filled(dict_of_inputs: dict) -> bool:
    """Returns a boolean telling if a dict is completely filled."""
    info_size = len(dict_of_inputs)
    filled_size = len(
        [value for value in dict_of_inputs.values() if value is not None]
    )
    return info_size == filled_size


def read_inputs_for_dict(dict_of_info: dict):
    """Reads information for a dict from user input."""
    for key in dict_of_info.keys():
        if dict_of_info[key] is not None:
            continue
        try:
            dict_of_info[key] = int(input(f"Qual a {key} atual? ").strip())
        except ValueError:
            log.error(f"[Error] {key.capitalize()} inválida")
            break  # para o for


info = {"temperatura": None, "umidade": None}

print("{:-^50}".format("Alarme De Temperatura"))


while not is_completely_filled(info):
    read_inputs_for_dict(info)

temp, umidade = info.values()  # unpacking [30, 90]

if temp > 45:
    print("ALERTA!!! 🥵 perigo calor extremo")
elif temp > 30 and (temp * 3) >= umidade:
    print("ALERTA!!! 🥵♒ Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("😀 Normal")
elif temp >= 0 and temp <= 10:
    print("🥶 Frio")
else:
    print("ALERTA!!! ☃️ Frio extremo")

print("#" * 50)
sys.exit(0)
