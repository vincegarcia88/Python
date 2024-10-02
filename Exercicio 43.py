'''Desenvolva um programa que leia 3 valores e mostre o menu:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
O programa deve realizar a operação solicitada em cada caso.'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))

while True:
    print('--- MENU ---')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair')
    opcao = int(input('---> '))

    if opcao == 1:
        soma = num1 + num2 + num3
        print(f'{num1} + {num2} + {num3} = {soma}\n\n\n')
    if opcao == 2:
        multiplicacao = num1 * num2 * num3
        print(f'{num1} x {num2} x {num3} = {multiplicacao}\n\n\n')
    if opcao == 3:
        maior = menor = num1
        if num2 > maior:
            maior = num2
        '''if num2 < menor:
            menor = num2'''
        if num3 > maior:
            maior = num3
        '''if num3 < menor:
            menor = num3'''
        print(f'O maior número digitado foi o {maior}\n\n\n')
        # print(f'O menor número digitado foi o {menor}\n\n\n')

    if opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        num3 = int(input('Digite outro número: '))
        print('\n\n\n')

    if opcao == 5:
        break
print('Volte sempre...')