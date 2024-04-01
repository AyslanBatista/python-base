# python -m pdb tembug.py | Ferramenta de debug | "help" para ver o comandos
# python -m pdb -c "until 12" tembug.py | Rodar até a linha 12
# python -m pdb -c continue tembug.py | Programa continua em caso de erro
# b 12 -> Breakpoint na linha 12
# s -> Para adentrar no escopo de uma função
# n -> Next para continuar parte por parte
# c -> Continue até o fim do programa ou até um breakpoint
# q -> Para sair do pdb
# disable 1 -> Para remover um breakpoint
breakpoint()  # Utiliza em uma parte do codigo para abrir o pdb

# pip install ipdb | export PYTHONBREAKPOINT=ipdb.set_trace
# pip install pudb | Modo grafico
# pip install winpdb | Ambiente Windowns


# Debug com print
def repete_vogal(word):
    """Retorna a palavra com as vogais repetidas."""
    final_word = ""
    for index, letter in enumerate(word):
        # usamos enumerate para ajudar a sabermos as voltas do loop
        print(f"{index=} {letter=}")
        if letter.lower() in "aeiouãõâôêéáíó":
            final_word = letter * 2
        else:
            final_word = letter
        print(f"{final_word=}")
    return final_word


print(repete_vogal("banana"))
