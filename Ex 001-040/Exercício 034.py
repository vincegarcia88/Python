#Faça um programa que leia 10 números e
#conte quantos deles são pares.

#Minha versão
for c in range (2,11, 2):
    print (c)

#Versão do professor
contaPares = 0

for c in range (0,10):
    numero = int(input ("Digite um número: "))
    if numero % 2 == 0:
        contaPares += 1

print (f"Insere {contaPares} números pares.")
