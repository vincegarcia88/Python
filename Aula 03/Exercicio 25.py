#Crie um programa que leia um numero
#inteiro e mostre se é par ou impar.

# Solicita ao usuário para inserir um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")