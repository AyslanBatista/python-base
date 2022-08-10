#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__version__ = "0.1.1"
__author__ = "Ayslan"
__license__ = "Unlicense"

# Dados
salas = {
    "sala1" : ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2" : ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aulas = {
    "aula_ingles" : ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "aula_musica" : ["Erik", "Carlos", "Maria"],
    "aula_danca" : ["Gustavo", "Sofia", "Joana", "Antonio"]
    
}

atividades = {
    "Inglês": aulas["aula_ingles"],
    "Música": aulas["aula_musica"],
    "Dança": aulas["aula_danca"],
    }

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades.items():
    print("{:^55}".format(f"Alunos da atividade {nome_atividade}"))
    print("-" * 55)

# sala1 que tem interseção com a atividade | Dois modos de fazer com set
    atividade_sala1 = set(salas["sala1"]) & set(atividade)
    atividade_sala2 = set(salas["sala2"]) & set(atividade)

    print(f"{nome_atividade} sala 1:", sorted(atividade_sala1))
    print(f"{nome_atividade} sala 2:", sorted(atividade_sala2))
    print("-" * 55)
