#Faça um programa que leia o ano de
#nascimento de 7 pessoas e mostre
#quantas são maiores de idade e quantas
#não são maiores de idade.

from datetime import date

maiorIdade = menorIdade = 0
dataAtual = date.today()
anoAtual = dataAtual.year

print (anoAtual)

for c in range (0,7):
    anoNascimento = int(input("Digite o seu ano de nascimento: "))
    if anoNascimento < anoAtual:
        if anoAtual - anoNascimento >= 18:
            maiorIdade += 1
        else:
            menorIdade += 1

    else:
        print("ALDRABOUM!")
        c=c -1

print(f"{maiorIdade} pessoas são maiores de idade.")
print(f"{menorIdade} pessoas é/são menores de idade.")