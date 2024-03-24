#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Ayslan"
__license__ = "Unlicense"

import sys

# EAFP - Easy to ASk Forgiveness than permission -
# É mais fácil perdir perdão do que permissão

try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))


try:
    print("O arquivo existe")  # FileNotFoundError
    # input("...")  # Race Condition
    names = open("names.txt").readlines()
    1 / 1  # ZeroDivisionError
    print(names.append)  # AttributeError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:  # Bare except
    print("[Error]: Missing name in the list")
    sys.exit(1)
