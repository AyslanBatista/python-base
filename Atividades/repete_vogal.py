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
import sys

Palavras = []

while True:
    new_palavra = ""
    palavra = input("Digite uma palavra (ou enter para sair):").strip()
    
    #Validacao
    if palavra.isdigit():
        print(f"[Error] Este valor {palavra} é invalido, informe apenas palavras")
        sys.exit(1)
    #Condição de parada
    if not palavra:
        break
    #Codigo Principal
    for letra in palavra:
    # TODO: Remover acentuação usando função
    # if ternário alternativo
        new_palavra += (
            letra * 2
            if letra.lower() in "aeiouãêóíáé"
            else letra
            )
    '''if normal
        if letra.lower() in "aeiouãêóíáé":
            new_palavra += letra * 2
        else:
            new_palavra += letra'''
    
    Palavras.append(new_palavra)
    

# Desempacotar uma lista, e utilizar o separador como uma quebra de linha
print(*Palavras, sep="\n")
    