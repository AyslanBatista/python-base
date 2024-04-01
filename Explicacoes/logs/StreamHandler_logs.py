#!/usr/bin/env python3
import logging
import os

# BOILERPLATE - Codigo repetitivo
"""Congiguração de logs que será exibido no console"""

# Controle de logs do usuario pela variavel de ambiente
# export LOG_LEVEL=debug
# export serve para ativar o log level em formato DEV, para exibir os debug
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger("logs.py", log_level)  # Criando stancia de log

ch = logging.StreamHandler()  # Handler responsavel por enviar para o console
ch.setLevel(log_level)  # Setando o level do Handler

# Objeto de formatação de como será exibido os logs
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

ch.setFormatter(fmt)  # Adicionando a formtação ao Handler que foi criado
log.addHandler(ch)  # Por fim adiciona o Handler ao log


"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execução")
log.critical("Erro geral ex: banco de dados sumiu")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    # stderr =  Erros
    log.error("Deu erro %s", str(e))
    # stdout = print
    print(f"[ERRO] Deu erro {str(e)}")
