# set, dict, list -> Mutaveis
sets = set()
sets.add(1)

dicionario = {}
dicionario["key"] = "value"

lista = []
lista.append(0)


# Criando uma lista nova no escopo local da função,
# se for passado uma lista vazia no valor default ela irá acumular o valor
# EX: def adiciona_a_lista(valor, lista=[]):
def adiciona_a_lista(valor, lista=None):
    if lista is None:
        lista = []
    lista.append(valor)
    return lista


adiciona_a_lista(4)
adiciona_a_lista(5)
print(adiciona_a_lista(6))
