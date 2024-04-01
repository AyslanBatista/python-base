# Função coringa que pode receber uma quantidade ilimitada de parametros
# Ex: Função print é uma função coringa | print("teste", "alo", 1, [])
# *args vai receber todo tipo ilimitado de parametros
# timout=10  precisar se nomeado na chamada da função
# **kwargs vai receber todo tipo de parametro nomeado e salvar em um dict
def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(item)

    print(kwargs)

    print(f"timeout {timeout}")


funcao(
    "bruno", 1, True, [], timeout=90, nome="Joao", cidade="Viana", data="Hoje"
)
