'''Crie um programa que leia o nome e a média de um aluno, calculando a sua
situação, tudo dentro de um dicionário.

No final mostre todo o conteúdo do dicionário.

Situação:
Média >= 9,5 – Aprovado
Média < 9,5 - Reprovado'''

aluno = dict()

aluno ["Nome"] = input("Insira o nome do aluno: ")
aluno ["Media"] = float (input("Digite a media: "))
aluno ["Situation"]

nota1 = int(input("\nInsira a nota do aluno: "))
nota2 = int(input("Insira a segunda nota do aluno: "))

media = float(nota1 + nota2) / 2
print (f"\nA média é:", media)

if media > 5:
    situation = "Aprovado!"
    print ("Parabéns! Você foi aprovado!")

else:
    situation = "Reprovado!"
    print ("Você foi reprovado!")

print (aluno.items)