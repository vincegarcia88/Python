
"""Crie um programa com uma função que vai funcionar como a função input(), no
entanto vai fazer a validação para aceitar apenas um valor numérico."""

def imita_input(msg):
    while True:
        numero = input(msg)
        if numero.isdigit():
            return int(numero)
        elif numero.isnumeric():
            return int(numero)
        else:
            continue


meu_numero = imita_input('Digite um número: ')

print(meu_numero)