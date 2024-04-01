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
print("Estilo funcional")
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

print()

# estilo procedural - Utiliza menas memoria
print("Estilo procedural")


def starts_with_b(text):
    """Return bool if text starts with b"""
    return text[0].lower() == "b"
    # return text.lower().startswith("b")


filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)
