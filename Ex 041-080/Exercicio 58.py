'''Crie um programa onde o utilizador insira 5 números dentro de uma lista.

Os valores devem ser registados já na posição correta [ordem crescente] e no
final mostre a lista ordenada.

Não utilizar o sort()'''

lista = list ()

for c in range (0, 5):
    numero = int(input(f"Digite {c+1}º número: "))
    if c == 0:
        lista.append (numero)
        print ("O número foi adicionado...")
    if numero > lista [-1]:  #-1 é a posição do número na lista
        lista.append (numero)
        print ("O número foi adicionado no fim...")

    else:
        indice = 0
        while indice < len (lista):
            if numero <= lista[indice]:
                lista.insert(indice, numero)
                print (f"O número foi adicionado na posição {indice + 1}")
                break
            indice += 1

print (lista)

