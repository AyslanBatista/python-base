#!/usr/bin/env /home/ayslan/Documentos/Virtual_Env_Python/PythonBase/bin/python3

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
__version__ = "0.0.1"
__author__ = "Ayslan Batista"
__license__ = "Unlicense"

# os >> Serve para ter acessos ao sistema operacional
import os

# pegando apenas os 5 primeiros caracter da variavel, mesmo que a variavel não exista ele ira retorna o padrão em ingles
current_language = os.getenv("LANG", "en_US")[:5]
# snake case

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
