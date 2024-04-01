#!/usr/bin/env python3
"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex: python repete_vogal.py

'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""

Palavras = []


print("{:#^50}".format("Repete Vogais 🔤 "))
while True:
    nova_palavra = ""

    palavra = input("Digite uma palavra (ou enter para sair): ").strip()
    if palavra.isdigit():

        print(
            f"[ERROR] Palavra informa: {palavra}.\n"
            "Informe apenas palavras que contenham letras !!!"
        )
        continue

    if not palavra:
        break

    for letra in palavra:

        nova_palavra += letra * 2 if letra.lower() in "aeiouãêóíáé" else letra

    Palavras.append(nova_palavra)

print(*Palavras, sep="\n")
