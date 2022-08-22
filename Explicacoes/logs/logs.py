#!/usr/bin/env python3
import logging
import os
from logging import handlers

#BOILERPLATE
# TODO: Mover para um modulo de utilidades
# Controle de logs para o usuario que irá fazer a execução do programa
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# Nossa instancia de log
log = logging.Logger("ayslan", log_level)
# level
#ch = logging.StreamHandler() #ConsoleLog = lugar onde será exibido, no caso sera terminal/stderr

fh = handlers.RotatingFileHandler(
    "meulog.log", #Nome do arquivo
    maxBytes=10**6,#maxBytes = 10**6 >> Tamanho maximo do arquivo, depois disso ele cria outro arquivo
    backupCount=10 #backupCount=10 >> Quantidade de arquivos para manter no backup
    ) 

#ch.setLevel(log_level) #Nivel que será exibido
fh.setLevel(log_level)
# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt) # Adicionando a formatação de log
fh.setFormatter(fmt)
# destino
#log.addHandler(ch)
log.addHandler(fh)

# root logger
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
