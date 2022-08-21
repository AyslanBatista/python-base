# aqui começa o escopo global
nome = "Global"
numero = 1
flag = True

def funcao():
    # aqui começa o escopo local
    nome = "Local"
    
    def funcao_interna(): #inner function # closure
        # aqui começa o escopo local da função interna
        nome = "Interna"
        print("Escopo local da funcao interna", locals())
        print("*" * 30)
        print(nome)
        return nome
        # aqui termina o escopo local da funcao interna
        
    
    print("Escopo local da funcao", locals())
    print("=" * 30)
    funcao_interna()
    print(nome)
    return nome
    # aqui termina o escopo local

# Verificar todas as variaveis globais
print("Escopo global do programa", globals())
print("-" * 30)

funcao()

print(nome)
print(globals()["nome"])

# aqui termina o espoco global