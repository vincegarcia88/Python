"""Crie um programa que tenha uma função que receba o nome de um aluno e uma
lista das suas notas. Ele deve calcular a média do aluno e mostrar no ecrã o
nome do aluno, a sua média e se ele ficou aprovado ou não."""

def mostra_notas(nome, notas):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)


    aluno = dict()
    aluno['Nome'] = nome
    aluno['Média'] = media
    aluno['Situação'] = 'Aprovado' if media >= 9.5 else 'Reprovado'

    for k, v in aluno.items():
        print(f'{k} -> {v}')


nome_aluno = input('Digite o nome do aluno: ')
notas_aluno = list()
for c in range(0, 5):
    nota_aluno = float(input('Digite uma nota: '))
    notas_aluno.append(nota_aluno)

mostra_notas(nome_aluno, notas_aluno)