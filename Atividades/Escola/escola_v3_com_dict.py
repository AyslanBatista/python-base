#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequenta cada uma das
atividades.
"""
__version__ = "0.1.2"
__author__ = "Ayslan Batista"
__license__ = "Unlicense"

# Dados
salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica": ["Erik", "Carlos", "Maria"],
    "Danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}


# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades.items():

    print(f"Alunos da atividade {nome_atividade}\n")

    atividade_sala1 = set(salas["sala1"]).intersection(atividade)
    atividade_sala2 = set(salas["sala2"]).intersection(atividade)

    print(f"Sala1 {atividade_sala1}")
    print(f"Sala2 {atividade_sala2}")
    print("-" * 60)
