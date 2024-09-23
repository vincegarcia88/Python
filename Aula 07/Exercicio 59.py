'''Crie um programa que leia vários números e coloca-os numa lista.

Crie duas listas adicionais que vão conter os números pares e impares da
lista principal. No final mostre todas as listas.'''

lista = list()
listaPares = list ()
listaImpares = list()

for c in range (0,10):
    novoNumero = int(input(f"Digite o {c+1} º número: "))
    lista.append(novoNumero)

    if novoNumero %2 == 0:
        listaPares.append (novoNumero)

    else: listaImpares.append(novoNumero)

print (f"Lista completa: {lista}")
print (f"Lista dos pares: {listaPares}")
print (f"Lista dos impares: {listaImpares}")

