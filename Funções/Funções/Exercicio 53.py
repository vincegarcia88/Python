'''Crie um programa que gere 5 números
aleatórios dentro de um tuple. Depois
mostra a listagem de números gerados, o
menor e o maior.'''

from random import randint

lista = (randint(1,50), randint(1,50),
         randint(1,50), randint(1,50),
         randint(1,50))

maior = menor = lista[0]

for elemento in lista:
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento

print('Os números aleatórios são: ', end='')
for elemento in lista:
    print(elemento, end=' ')

print(f'\nO maior elemento da lista é o: {maior}')
print(f'O menor elemento da lista é o: {menor}')