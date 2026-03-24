"""
Programa: adulto
Descrição: este programa pergunta a idade de uma pessoa. Se a idade for maior do que 18 anos, o programa imprime na tela o texto "Oi! Você é um adulto.”
Data: 24/03/2026
Versão: 0.0.1

"""


# Alocação de memória

idade = 0
texto = ""


# Entrada de dados

idade = int(input("\nQual a sua idade? "))


# Processamento de dados

if idade >= 18:
    texto = 'Oi! Você é um adulto.'
    

    # Saída de dados

print(texto)