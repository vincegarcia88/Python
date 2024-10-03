#Return

def calcula_media(notas):
    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)
    return media

def calcula_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    return media


def mostra_situacao(media):
    if media >= 9.5:
        print('Aprovado')
    else:
        print('Reprovado')


notas_aluno = [9, 9, 9, 9]
media_aluno = calcula_media(notas_aluno)

mostra_situacao(media_aluno)
