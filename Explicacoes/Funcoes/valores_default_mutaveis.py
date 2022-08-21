# set, dict, list -> Mutaveis
s = set()
s.add(1)

d = {}
d["key"] = "value"

l = []
l.append(0)

# Criando uma lista nova no escopo local da função,
# se for passado uma lista vazia no valor default ela irá acumular o valor
def adiciona_a_lista(valor, lista=None):
    if lista is None:
        lista = []
    lista.append(valor)
    return lista

adiciona_a_lista(4)
adiciona_a_lista(5)
print(adiciona_a_lista(6))

