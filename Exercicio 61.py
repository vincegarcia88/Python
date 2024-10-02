'''Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz com a formatação adequada.'''

matriz = list()

for linha in range(0, 3):
    numeros = list()
    for coluna in range(0, 3):
        numero = int(input(f'Digite um número para a linha {linha} coluna {coluna}: '))
        numeros.append(numero)
    matriz.append(numeros)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]}', end='\t')
    print()