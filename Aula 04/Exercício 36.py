#Faça um programa que mostre a tabuada
#de um número introduzido pelo
#utilizador.

num1 = int(input("Insira um número: "))

for c in range (0,10):
    print (f"{num1}x{c} = {num1 * c}")

    # PRINT (F"{num1} x {c+1} = {num1 * c+1}")
    #O professor fez com +1 (Não entendi)