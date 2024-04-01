#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Ayslan"
__license__ = "Unlicense"

import logging
import sys
import time

log = logging.Logger("erros")

# EAFP - Easy to ASk Forgiveness than permission -
# É mais fácil perdir perdão do que permissão


# Retry com FOR
def try_to_opan_a_file_for(filepath, retry=1) -> list:
    """Tries to open a sile, if error, retries n times."""
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readlines()
        except FileNotFoundError as e:
            log.error("ERRO: %s", e)
            time.sleep(1)
        except ZeroDivisionError:
            print("[Error] You cant divide by zero!!!")
            sys.exit(1)
        except AttributeError:
            print("[Error] List doesn't have banana")
            sys.exit(1)
        else:
            print("Sucesso!!!")
        finally:
            print("Execute isso sempre!")
    return []


# Retry com Recursão
def try_to_opan_a_file(filepath, retry=1) -> list:
    """Tries to open a sile, if error, retries n times."""
    if retry > 999:
        raise ValueError("Retry cannot be above 999")

    try:
        return open(filepath).readlines()
    except FileNotFoundError as e:
        log.error("ERRO: %s", e)
        time.sleep(1)
        if retry > 1:
            return try_to_opan_a_file(filepath, retry=retry - 1)
        # DEADLOCK | ERRO DE RECURSÃO
    except ZeroDivisionError:
        print("[Error] You cant divide by zero!!!")
        sys.exit(1)
    except AttributeError:
        print("[Error] List doesn't have banana")
        sys.exit(1)
    else:
        print("Sucesso!!!")
    finally:
        print("Execute isso sempre!")
    return []


for line in try_to_opan_a_file("names.txt", retry=5):
    print(line)

names = ["ayslan", "bruno", "test"]
try:
    print(names[2])
except (ZeroDivisionError, AttributeError):
    print("[Error]: Missing name in the list")
    sys.exit(1)

# Forçar um erro | Serve para subir um erro por conta propria
try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))
