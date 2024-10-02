'''Crie um programa que leia 5 números e guarde-os
numa lista. No final mostre o maior e o menor valor e a
respectiva posição na lista.'''

import random

#Random numbers

lista = list(random.randint(1,20) for _ in range (9))
print(lista)

#From the minor
lista.sort()
print (lista)

#From the major
lista.reverse()
print(lista)

'''------------------------------'''


'''numeros = list () 
maior = menor = posMaior = posMenor = contador = 0

for c in range (0,5):
    numeros [c] = int(input(f"Digite o {c+1}ª número: "))
    if c == 0:
        maior = menor 0 numeros [c]

    else:
        for numero in numeros:
            if numero > maior:
                maior = numero
                posMaior = contador
            if numero < menor:
                menor = numero
                posMenor = contador
            contador += 1'''

