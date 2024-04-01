#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Ayslan"
__license__ = "Unlicense"

import os
import sys

# LBYL - Look Before You Leap >> Olhe antes de atravessar a rua |
# Antes de fazer uma operação verifique se é possível fazer essa operação
if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...")  # Race Condition
    names = open("names.txt").readlines()
else:
    print("[Error]: File names.txt not found.")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error]: Missing name in the list")
    sys.exit(1)
