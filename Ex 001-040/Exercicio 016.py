#Cria um programa que leia 5
#notas introduzidas pelo
#utilizador e que calcule a
#média aritmética entre eles.

#Pedir as notas
nota1 = float(input("Insira sua primeira nota: "))
nota2 = float (input("Insira sua segunda nota: "))
nota3 = float (input("Insira sua terceira nota: "))
nota4 = float (input ("Insira sua quarta nota: "))
nota5 = float (input("Insira sua quinta nota: "))

#Calcular a média
media = (nota1+nota2+nota3+nota4+nota5)/5

#Apresentar a média
print("A sua média é", media, ".")
if media < 5:
    print ("Você foi reprovado!")
elif media > 5:
    print ("Parabéns, você foi aprovado!")

