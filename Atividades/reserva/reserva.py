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
import sys

path = os.curdir
filepath_quartos = os.path.join(path, "quartos.txt")
filepath_reserva = os.path.join(path, "reservas.txt")

# Apresentação
while True:
    print("{:-^60}".format("Hotel - Reserva para Dev's"))
    for line in open(filepath_quartos):
        l_numero, l_quarto, l_valor = line.split(",")
        print(
            "{:^60}".format(
                f"Numero:{l_numero} | Modelo:{l_quarto} | Valor:R${l_valor}"
            )
        )
    print("-" * 60, "\n")

    # Variaveis
    cliente = input("Qual seu nome: ").strip()
    sair = True
    while sair == True:
        
        numero_quarto = int(input("Qual o número do quarto a ser reservado: "))
        for line in open(filepath_reserva).readlines():
            r_cliente, r_numero, r_qtd_dias = line.split(",")
            if numero_quarto == int(r_numero):
                print("Desculpe esse quarto não está disponível no momento")
                sair = True
                break
            else:
                sair = False
        

    qtd_dias = int(input("Qual a quantidade de dias: "))

    for line in open(filepath_quartos):
        numero, quarto, valor = line.split(",")
        if numero_quarto == int(numero):
            valor_total = int(valor) * qtd_dias
            print(
                f"Reserva do quarto {quarto} por {qtd_dias} dias "
                f"fica no valor de total de R${valor_total}"
            )
            break

    confirmacao = input("Deseja confirmar a reserva? (y/n)").strip()
    if confirmacao.lower() == "n":
        continue
    elif confirmacao.lower() == "y":
        with open(filepath_reserva, "a") as file_:
            file_.write(f"{cliente},{numero},{qtd_dias}" + "\n")
        print(
            f"\nReserva do quarto Numero:{numero} - `{quarto}` por {qtd_dias} "
            f"dias, para o cliente {cliente} registrada com Sucesso!\n"
        )
        print("#" * 60)
        sys.exit(0)
