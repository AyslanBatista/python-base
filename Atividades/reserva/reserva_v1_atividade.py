#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponíveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.

`quartos.txt`

```
# codigo, nome, preco
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50
```
O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`

```
# cliente, quarto, dias
Bruno,3,12
```

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.

"""

import os

path = os.curdir
filepath_quartos = os.path.join(path, "quartos.txt")
filepath_reserva = os.path.join(path, "reservas.txt")

lista_reservados = open(filepath_reserva).readlines()

reservados = []
if lista_reservados[1:]:
    for n in lista_reservados[1:]:
        cliente, quarto_reserv, dias = n.strip().split(",")
        reservados.append(quarto_reserv)


quartos = open(filepath_quartos).readlines()

menu = []
for quarto_menu in quartos[1:]:
    if quarto_menu[0] in reservados:
        quarto_menu += " (reservado)"
        menu.append(quarto_menu.replace("\n", ""))
    else:
        menu.append(quarto_menu.strip())


print("{:#^50}".format(" HOTEL DO PROGRAMADOR 🏨🌄 "))
print("Ola, seja bem vindo 😃!!!\n")
print(*menu, sep="\n")

nome = input("\nPor favor, informe seu nome: ")

while True:
    quarto = input("Informe o numero do quarto que deseja alugar: ")
    if quarto in reservados:
        print(
            f"Quarto numero {quarto} já está reservado, "
            "por favor escolha um quarto que esteja disponivel"
        )
        continue
    break

dias = int(input("Por quantos dias deseja alugar: "))

print("\nSeu quarto foi reservado com sucesso! 🫡")
for n in quartos[1:]:
    num, suite, valor = n.strip().split(",")
    if quarto == num:
        total_pagar = dias * int(valor)
        print(f"Valor total para pagamento: R$ {total_pagar:.2f}")

with open(filepath_reserva, "a") as file_:
    file_.write(f"{nome},{quarto},{dias}\n")
