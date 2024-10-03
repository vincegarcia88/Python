'''from math import factorial

numero = int(input("Digite um número: "))
print(f"O fatorial com função é: {factorial(numero)}")'''

from math import factorial

numero = int(input('Digite um número: '))
print(f'O fatorial com função é: {factorial(numero)}')

contador = numero
fatorial = 1

print(f'{numero} x ', end='')

while contador > 1:
    fatorial *= contador
    contador -= 1
    if contador == 1:
        print(f'{contador} = {fatorial}', end='')
    else:
        print(f'{contador} x ', end='')