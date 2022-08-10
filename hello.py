#!/usr/bin/env python3

"""Hello Wordl Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR
    
Ou informe atraves do CLI argument `--lang'.

Ou o usuário terá que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py
    
"""
__version__ = "0.1.3"
__author__ = "Ayslan"
__license__ = "Unlicense"

# os >> Serve para ter acessos ao sistema operacional
import os
import sys

# DEBUG
# Comando abaixo serve para pegar todo informação que for passada na linha de comando ao rodar o programa
# print(f"{sys.argv=}")

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    #Desempacotando os valores e depois separando pelo "=" os argumentos que são passados ao rodar o programa
    key, value = arg.split("=")
    
    #lstrip removendo os "-" do começo, strip() Removendo os espaços em branco
    key = key.lstrip("-").strip()
    value = value.strip()
    
    # Validando os argumentos que são passados, caso não seja um agumento que não esteja no dict arguments retorna um erro
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

# [:5] pegando apenas os 5 primeiros caracter da variavel | "en_US" mesmo que a variável não exista ele ira retorna o padrão em inglês
current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input(
            "Choose a language:\n"
        )
    
current_language = current_language[:5]

# sets (Hash Table) - O(1) - constante
# dicts (Hash Table)

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}


# 0(1) - constante - 'in' - Get item
print(msg[current_language] * int(arguments["count"]))
