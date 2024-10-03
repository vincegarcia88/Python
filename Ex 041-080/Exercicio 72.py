"""Crie um programa que tenha uma função que receba 3 parâmetros: inicio, fim e
passo. O programa deve realizar 3 contagens através da função.

a) De 1 até 20, de 2 em 2
b) De 10 até 0, de 1 em 1
c) Contagem personalizada"""


def contagem(inicio, fim, passo):
    # Ajusta o passo caso seja zero
    if passo == 0:
        passo = 1 if inicio < fim else -1

    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')
    for c in range(inicio, fim + (1 if passo > 0 else -1), passo):
        print(c, end=' ')
    print('\n' + '-' * 30)


# Programa principal
# a) Contagem de 1 até 20, de 2 em 2
contagem(1, 20, 2)

# b) Contagem de 10 até 0, de 1 em 1
contagem(10, 0, -1)

# c) Contagem personalizada pelo usuário
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contagem(inicio, fim, passo)
