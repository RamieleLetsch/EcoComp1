

"""
Programa: criança
Descrição: O programa pergunta a idade de uma pessoa e, Se esta for maior que ou igual a 18 anos, imprime na tela ”Oi! Você é um adulto.”. Caso contrário, imprima "Oi! Você é menor de idade.”
Autor: Ramiele D. Letsch
Data:24/03/2026
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
else:
    texto = 'Oi! Você é menor de idade.'


# Saída de dados
print(texto)