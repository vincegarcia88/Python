#Crie um programa que leia 5 notas de
#um aluno e calcule a sua média.

#>=9.5 passou
#>8 e < 9.5 em recuperação
#<8 reprova

from time import sleep

nota1 = float(input("Insira sua 1a nota: "))
nota2 = float(input("Insira sua 2a nota: "))
nota3 = float(input("Insira sua 3a nota: "))
nota4 = float(input("Insira sua 4a nota: "))
nota5 = float(input("Insira sua 5a nota: "))

media = (nota1+nota2+nota3+nota4+nota5)/ 5
print ("Calculando a média...")
sleep (2)
print (media)

if media >=9.5:
    sleep (1)
    print ("Aprovado!")

elif media <8:
    sleep (1)
    print ("Em recuperação!")

else:
    sleep (1)
    print ("Reprovado!")