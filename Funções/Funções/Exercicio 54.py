'''Crie um programa que leia 4 valores e
guarde-os num tuple. No final exiba:

a) Quantas vezes aparecer o número 7.
b) Em que posição foi digitado o número 5.
c) Quais são os números pares.

O programa deve informar quando não
encontrar resposta.'''

lista = (int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')), int(input('Digite um número: ')))

# Conta as ocorrencias do número 7
if lista.count(7) <= 0:
    print('O número 7 não aparece.')
else:
    print(f'O número 7 aparece {lista.count(7)} vezes.')

# Mostra a posição do número 5
if 5 not in lista:
    print('O número 5 não aparece.')
else:
    print(f'O número 5 aparece na posição {lista.index(5) + 1}')

# Mostra os pares
print('Os números pares são: ', end='')
contador = 0

for numero in lista:
    if numero % 2 == 0:
        print(f'{numero}', end=' ')
        contador += 1

# Apenas imprime se não houver pares encontrados
if contador == 0:
    print('Nenhum par encontrado')

