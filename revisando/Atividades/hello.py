#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe
a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe atraves do CLI argument `--lang`

Ou o usuário terá que digitar

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.4"
__author__ = "Ayslan Batista"
__license__ = "Unlicense"

import logging
import os
import sys

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("ayslan", log_level)
ch = logging.StreamHandler()  # ConsoleLog = lugar onde será exibido
ch.setLevel(log_level)  # Nivel que será exibido
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)  # Adicionando a formatação de log
log.addHandler(ch)


arguments = {
    "lang": None,
    "count": 1,
}

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde",
}

for arg in sys.argv[1:]:

    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use `=`, you passed %s, try with --key=value: %s",
            arg,
            str(e),
        )
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]


# EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)


"""
# Try com valor default
message = msg.get(
    current_language, msg["en_US"]
)
"""

# O(1) - constante - `in`
print(message * int(arguments["count"]))
