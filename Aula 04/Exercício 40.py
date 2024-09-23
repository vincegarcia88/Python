#Faça um programa que leia a idade de
#10 pessoas. No final mostre qual foi a
#maior idade lida e a menor.

maiorIdade = 0
menorIdade = 0

for c in range (0,10):
    idade = int(input("Digite a sua idade: "))
    if c == 0:
        maiorIdade = idade
        menorIdade = idade

    else:
        if idade > maiorIdade:
            maiorIdade = idade

        if idade < menorIdade:
            menorIdade = idade

print("")
print (f"A maior idade ida foi: {maiorIdade}.")
print (f"A menor idade ida foi: {menorIdade}.")