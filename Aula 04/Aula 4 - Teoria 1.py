
#laço c no intervalo (1,5)
 #   se buraco
 #       salta

 #   se não
 #       passo
 #===================

#O laço for é utilizado quando sabe quantas vezes um bloco de código deve ser executado.

for c in range (1,5):
    print ("Olá!")

for c in range (1,5):
    print (c)

#Tabuada
num = int(input("Digite um número: "))

for c in range (1,11):
    print(f"{num}x{c} = {num * c}")

#=====*=====*=====*=====*=======*======*=====*

#Código a corrigir
inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))

for c in range (5,20):
    print (c)
print ("")


#==========*=======*=====*=====*

#O até 100 de 2 em 2:
inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
passo = int(input("De quanto em quanto: "))

for c in range (inicio, fim +1, passo):
    print(c)

print("")

#==*==*==*==*==*==*==*==*

#Exemplo

fim = int (input("Digite a quantidade de números que quer ler: "))
soma = 0

for c in range (1, fim + 1):
   numero = int(input(f"Digite o {c}ª número: "))
   soma = soma + numero
print(f"A soma vale: {soma}.")
