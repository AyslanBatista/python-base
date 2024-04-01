#!/usr/bin/env python3
# python -m smtpd -c DebuggingServer -n localhost:8025

"""Exemplos de envio de e-mail"""

import smtplib

SERVER = "localhost"
PORT = 8025  # 25 TCP PADRAO DE E-MAIL | 8025 para servidor de teste local


FROM = "bruno@rocha.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá mundo</b>
"""

# SMTP
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

print(message)

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
