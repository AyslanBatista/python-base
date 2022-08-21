"""Imprime apenas os nomes iniciados com a letra B"""

names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian",
]


# Filtrando a função com uma condição que retorna true,
# Transformando em lista e depois desempacotando cada nome no retorno

# estilo funcional
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

# estilo imperativo
def starts_with_b(text):
    return text[0].lower() == "b"
    # return text.lower().startswith("b")
