
"""Crie um programa com uma função que vai receber várias notas de alunos e vai
retornar um dicionário com o seguinte:

a) Quantidade de notas
b) A maior nota
c) A média da turma
d) A situação (lógico opcional)
>12 – boa
<9,5 – fraca
>9,5 e <12 - razoável"""

def quantidade_notas(notas):
    return len(notas)


def maior_nota(notas):
    maior = None
    for indice, nota in enumerate(notas):
        if indice == 0:
            maior = nota
        else:
            if nota > maior:
                maior = nota
    return maior


def media_turma(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)


def situacao(media):
    if media > 12:
        return 'Boa'
    elif media < 9.5:
        return 'Fraca'
    else:
        return 'Razoável'


def calcula_situacao(notas, mostra_situacao=False):
    dicionario = dict()
    dicionario['Quantidade de notas'] = quantidade_notas(notas)
    dicionario['Maior nota'] = maior_nota(notas)
    dicionario['Média'] = media_turma(notas)
    if mostra_situacao:
        dicionario['Situação'] = situacao(media_turma(notas))
    return dicionario


lista_notas = list()
for c in range(0, 5):
    nota = float(input('Digite uma nota: '))
    lista_notas.append(nota)

mostra = int(input('Deseja ver a situação da turma [1-sim/2-não] ->'))
mostra = True if mostra == 1 else False

analise_turma = calcula_situacao(lista_notas, mostra)

for k, v in analise_turma.items():
    print(f'{k} -> {v}')