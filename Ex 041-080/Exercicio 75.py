"""Crie um programa que tenha uma função que receba um número inteiro e mostre a
tabuada desse número."""

def tabuada(num):
    for c in range (0,10):
        print(f"{num} x {c+1} = {num * (c+1)}")

numero = None
while numero !=0:
    numero = int(input("\nDigite o numero para saber a tabuada: "))
    tabuada (numero)

