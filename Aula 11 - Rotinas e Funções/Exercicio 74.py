"""Crie um programa que tenha uma função que receba o nome de um aluno e uma
lista das suas notas. Ele deve calcular a média do aluno e mostrar no ecrã o
nome do aluno, a sua média e se ele ficou aprovado ou não."""

def calcula_media (nome, notas):
    soma = 0
    for nota in notas:
        soma += nota

    media = soma / len(notas)

    aluno = dict()
    aluno["Nome"] = nome
    aluno["Media"] = media
    aluno["Situação"] = "Aprovado" if media >=9.5 else "Reprovado"
    print(aluno)

    nome_aluno = input("Digite o nome do aluno: ")
    notas = list()

    While True:
        nota = float(input("Digite uma nota: "))
        notas.append(nota)
    print("Deseja continuar? [S/N")

    CORRIGIR