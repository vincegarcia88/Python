
#Trabalhar o IF, ELIF e ELSE

media = float(input("Insira sua nota: "))

if media >= 5:
    print ("Você foi aprovado!")
elif media< 5:
    print ("Reprovado!")

#Calcular a média

nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma nota: "))
nota3 = float(input("Digite uma nota: "))

media = (nota1+nota2+nota3)/3
print (f"A média é: {media} valores.")

# ELSE

idade = 17

if idade <=17:
    print ("Menor de idade")
elif idade <60:
    print ("Adulto")
else:
    print ("Velho!")

print
print

#
if media>= 8:
    print ("Passou!")

elif media <8:
    print ("Se fufu")

else:
    print("Em recuperação!")

print("Terminei o programa.")

print
print

#AND, OR e

faltas = 6
if media>= 8 and faltas <5:
    print ("Passou!")

else:
    print("Em recuperação!")

print("Terminei o programa.")