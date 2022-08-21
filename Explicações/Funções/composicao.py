names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian",
]

# TODO: Usar lambdas

def starts_with_b(text):
    return text[0].lower() == "b"
    # return text.lower().startswith("b")

# Filtrando a função com uma condição que retorna true,
# Transformando em lista e depois desempacotando cada nome no retorno
print(*list(filter(starts_with_b, names)))

