#Escreva um programa que leia um número N inteiro
#qualquer e mostre os N primeiros elementos
#de uma sequência de Fibonacci.

'''Cada número é a soma de seus dois antecessores'''

from time import sleep

#ler um número inteiro
numero = int(input("Digite um número: "))

#Pedir número que seja superior a 1, para validar o pedido anterior.

while True:
    if numero < 1:
        print("Número inválido.")
        numero = int(input("Digite um número inteiro maior que zero: "))
    else:
        break

#Fórmula para identificar os 2 antecessores
inicio = 1
anterior = 0
atual = 0
contador = 0

print(f"{inicio} -> ", end="")

while contador < numero:
    atual = inicio + anterior
    anterior = inicio
    inicio = atual
    contador += 1
print(inicio)

