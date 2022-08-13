#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Ayslan"
__license__ = "Unlicense"

import os
import sys

# EAFP - Easy to ASk Forgiveness than permission - É mais fácil perdir perdão do que permissão

try:
    names = open("names.txt").readlines()
    1 / 1 # ZeroDivisionError
    print(names.banana) # AttributeError
except FileNotFoundError as e: # Bare except - Qualquer tipo de exceção
    print("[Error]: File names.txt not found.")
    print(f"{str(e)}.")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You cant divide by zero!!!")
    sys.exit(1)
except AttributeError:
    print("[Error] List doesn't have banana")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")
    

try:
    print(names[2])
except (ZeroDivisionError, AttributeError) :
    print("[Error]: Missing name in the list")
    sys.exit(1)

# Forçar um erro | Serve para subir um erro por conta propria 
try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))