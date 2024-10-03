'''Crie um programa onde o utilizador possa digitar
vários números e guardá-los numa lista.

Caso o número inserido esteja na lista ele não deve ser
adicionado. No final mostre todos os valores por ordem DECRESCENTE.'''

lista = list()

contador = 0

while True:
    novoNumero = int(input(f"Digite o {contador + 1}º número: "))

    if novoNumero in lista:
        print (f"O número {novoNumero} já se encontra na lista.")
        continue

    else:
        contador
        lista.append(novoNumero)

    if contador == 9:
        break

contador += 1

lista.sort (reverse=True)

print (f"{lista}")
