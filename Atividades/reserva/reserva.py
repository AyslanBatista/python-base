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
import logging
import os
import sys


# Apresentação
while True:
    
    ocupados = {}
    try:
        for line in open("reservas.txt"):
            nome, num_quarto, dias = line.strip().split(",")
            ocupados[int(num_quarto)] = {  # Chave primary, com os valores
                "nome": nome,
                "dias": dias, 
            }
    except FileNotFoundError:
        logging.error("Arquivo reservas.txt não existe")
        sys.exit(1)            
    
    # SETANDO VARIAVEIS
    quartos = {}
    try:
        for line in open("quartos.txt"):
            l_numero, l_quarto, l_valor = line.strip().split(",")
            quartos[int(l_numero)] = {  # Chave primary, com os valores
                "nome": l_quarto,
                "preco": float(l_valor),  # TODO: Decimal
                "disponivel": False if int(l_numero) in ocupados else True
            }
    except FileNotFoundError:
        logging.error("Arquivo quartos.txt não existe")
        sys.exit(1)

    # PAINEL INICIAL
    print("{:-^60}".format("Hotel - Reserva para Dev's"))
    for codigo, dados in quartos.items():
        nome = dados["nome"]
        preco = dados["preco"]
        disponivel = "⛔️" if not dados["disponivel"] else "👍"
        # disponivel = dados['disponivel'] and "👍" or "⛔️"
        # TODO: Substituir casa decimal por virgula
        print(
            "{:^60}".format(
                f"Numero:{codigo} | Modelo:{nome} | Valor:R${preco:.2f} | {disponivel}"
            )
        )
    print("-" * 60, "\n")

    # RECOLHENDO INFORMAÇÃO DO USUARIO
    cliente = input("Qual seu nome: ").strip()
    sair = True
    while sair == True:
        try:
            numero_quarto = int(
                input("Qual o número do quarto a ser reservado: ")
            )
            if not quartos[numero_quarto]["disponivel"]:
                print(
                    f"Desculpe o quarto {numero_quarto} não está disponível no momento"
                )
                sair = True
                continue     
        except ValueError:
            logging.error("Número inválido, digite apenas digitos.")
            sys.exit(1)
        except KeyError:
            sair = True
            print(f"O Quarto {numero_quarto} não existe")
            continue
        sair = False
        
        
    try:
        qtd_dias = int(input("Qual a quantidade de dias: "))
    except ValueError:
        logging.error("Número inválido, digite apenas digitos.")

    for line in open("quartos.txt"):
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
        with open("reservas.txt", "a") as file_:
            file_.write(f"{cliente},{numero},{qtd_dias}" + "\n")
        print(
            f"\nReserva do quarto Numero:{numero} - `{quarto}` por {qtd_dias} "
            f"dias, para o cliente {cliente} registrada com Sucesso!\n"
        )
        print("#" * 60)
        sys.exit(0)
