#!/usr/bin/env python3
""" Template para enviar e-mail com informações de cada cliente

 Olá, Maria
    
    Tem interesse em comprar caneta?
    
    Este produto é ótimo para resolver
    Escrever muito bem
    
    Clique agora em https://canetaslegais.com
    
    Apenas 1 disponiveis!
    
    Preço promocional 50.50
"""
__version__ = "0.1.0"
__author__ = "Ayslan"
__license__ = "Unlicense"


email_tmpl = """
    Olá, %(nome)s
    
    Tem interesse em comprar %(produto)s?
    
    Este produto é ótimo para resolver
    %(texto)s
    
    Clique agora em %(link)s
    
    Apenas %(quantidade)d disponiveis!
    
    Preço promocional %(preco).2f
"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
        print(
            email_tmpl
            % {
                "nome": cliente,
                "produto": "caneta",
                "texto": "Escrever muito bem",
                "link": "https://canetaslegais.com",
                "quantidade": 1,
                "preco": 50.5,
                
            }
        )
        