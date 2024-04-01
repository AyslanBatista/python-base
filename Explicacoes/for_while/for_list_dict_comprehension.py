#!/usr/bin/env python3

# Diminuindo os recursos de memoria,ao invés de usar lista, use range
# numbers = [1,2,3,4,5,6]
numbers = range(1, 7)  # start, next, stop

print(numbers[-1])
print(numbers[2:])

# For loops / Laço for
# iterable
for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        # Quando chegar aqui e tiver o continue,
        # ele voltará para o for | Interceptar o loop
        continue
    print(f"mais codigo com {number}")


dados = {}
for line in open("post.txt"):
    if line == "---\n":
        # Quando chegar aqui e tiver o break, ele para o for definitivamente
        break
    key, valor = line.split(":")
    dados[key] = valor.strip()
print(dados)


original = [1, 2, 3]
# Estrutural
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# LIST COMPREHENSION
# Funcional | Essa operação só é boa quando o objetivo for criar *listas*
dobrada = [n * 2 for n in original]
print(dobrada)

# Dict COMPREHENSION
dados = {
    line.split(":")[0]: line.split(":")[1].strip()  # Key[0] : Value[1]
    for line in open("post.txt")
    if ":" in line
}

dados = {}
for line in open("post.txt"):
    if ":" in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()
print(dados)
