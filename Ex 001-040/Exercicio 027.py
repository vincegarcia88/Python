#Crie um programa que leia dois números
#inteiros e compare-os da seguinte
#forma:

#- O primeiro número é maior;
#- O segundo número é maior;
#- Os números são iguais.

num1 = int(input ("Insira um número: "))
num2 = int(input ("Insira outro número: "))

if num1 > num2:
    print (f"O número {num1} é maior que {num2}.")

elif num2 > num1:
    print (f"O número {num2} é maior que {num1}.")

else:
    print ("Os números são iguais.")