#Faça um programa que leia 5 números
#inteiros e mostre a soma desses números.

#Versão do professor
soma = 0
numeros = 0

for c in range (0,5):
    numeros = int(input(f"Digite o {c+1}ª número: "))
    soma = soma + numeros

print (f"A soma dos números é {soma}.")

print
print

#Minha versão

num1 = int(input ("Digite o 1º número: "))
num2 = int(input ("Digite o 2º número: "))
num3 = int(input ("Digite o 3º número: "))
num4 = int(input ("Digite o 4º número: "))
num5 = int(input ("Digite o 5º número: "))

soma = (num1+num2+num3+num4+num5)

for c in range (soma + 1):
    print (c)


