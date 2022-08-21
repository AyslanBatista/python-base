from socket import timeout


def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(item)

    print(kwargs)

    print(f"timeout {timeout}")


funcao(
    "bruno", 1, True, [], timeout=90, nome="Joao", cidade="Viana", data="Hoje"
)


def soma(a, b):
    return a + b


soma(1, 3)
soma(1, b=3)


def hello(nome, sobrenome="Sabugosa"):
    print(f"Hello {nome}, {sobrenome}")


hello("Bruno", "Rocha")
hello(sobrenome="Rocha", nome="Bruno")
hello("Bruno")
