#Faça um programa que leia um número
#inteiro e diga se ele é ou não um número primo.

num1 = int(input("Insira um número: "))
controle = 0

for c in range (0,num1):
    if num1 % (c+1) == 0:
        controle += 1

if controle == 2:
    print(f"O número {num1} É PRIMO.")

else:
    print(f"O número {num1} NÃO é primo.")