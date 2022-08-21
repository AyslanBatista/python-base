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
import logging
import os
import sys

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("ayslan", log_level)
ch = logging.StreamHandler()  # ConsoleLog = lugar onde será exibido
ch.setLevel(log_level)  # Nivel que será exibido
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)  # Adicionando a formatação de log
log.addHandler(ch)


# DEBUG
# Comando abaixo serve para pegar todo informação que for passada na linha de comando ao rodar o programa
# print(f"{sys.argv=}")

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # Desempacotando os valores e depois separando pelo "=" os argumentos que são passados ao rodar o programa
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use `=`, you passed %s, try --key=value: %s",
            arg, str(e)
        )
        sys.exit(1)

    # lstrip removendo os "-" do começo, strip() Removendo os espaços em branco
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
        current_language = input("Choose a language:\n")

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

# try, execept with value default
# message = msg.get(current_language, msg["en_US"])

# LBYL
# if current_language in msg:
#     massage = msg[current_language]
# else:
#     print(f"Language is invalid, chose from: {list(msg.keys())}")
#     sys.exit(1)

# EAFP
try:
    massage = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, chose from: {list(msg.keys())}")
    sys.exit(1)

# 0(1) - constante - 'in' - Get item
print(massage * int(arguments["count"]))
