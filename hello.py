#!/usr/bin/env python3

"""Hello Wordl Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR
    
Execução:

    python3 hello.py
    ou
    ./hello.py
    
"""
__version__ = "0.1.2"
__author__ = "Ayslan"
__license__ = "Unlicense"

# os >> Serve para ter acessos ao sistema operacional
import os

# [:5] pegando apenas os 5 primeiros caracter da variavel | "en_US" mesmo que a variável não exista ele ira retorna o padrão em inglês
current_language = os.getenv("LANG", "en_US")[:5]
# snake case

# sets (Hash Table) - O(1) - constante
# dicts (Hash Table)

msg ={
  "en_US": "Hello, World!",
  "pt_BR": "Olá, Mundo!",
  "it_IT": "Ciao, Mondo!",
  "es_SP": "Hola, Mundo!",
  "fr_FR": "Bonjour, Monde!"
  
}


# 0(1) - constante - 'in' - Get item
print(msg[current_language])
