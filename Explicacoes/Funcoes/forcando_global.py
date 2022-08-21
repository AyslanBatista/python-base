# Forcando global dentro da função
nome = "Global"

def funcao():
    nome = "Local"
    print("Nome Local:", nome)
    nome = globals()["nome"]
    print("Nome Global:", nome)
    
funcao()


numero = 0

def funcao2():
    global numero
    numero += 1
    subcontador = 0
    
    def funcao_interna():
        global numero
        numero += 1
        
        nonlocal subcontador
        subcontador += 1
        
    funcao_interna()
    
funcao2()
funcao2()
print(numero)
    

# Alterar o contador global
contador = 0

def incrementa_contador():
    # ... comeca o escopo local
    # assignment `=` `+=` `-=` | Quando existe operações que altera o valor,
    # é nescessario usar global ou ter um variavel local
    global contador
    contador += 1

incrementa_contador()
incrementa_contador()
incrementa_contador()
incrementa_contador()
print(contador)