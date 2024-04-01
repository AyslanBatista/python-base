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
words = []

while True:

    word = input("Digite uma palavra (ou enter para sair):").strip()

    if not word:
        break

    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        final_word += letter * 2 if letter.lower() in "aeiouãêóíáé" else letter

    words.append(final_word)


# Desempacotar uma lista, e utilizar o separador como uma quebra de linha
print(*words, sep="\n")
