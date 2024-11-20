"""Crie uma classe chamada “Aluno” que possua atributos para armazenar o nome e
as notas de um aluno. Adicione métodos para calcular a média das notas e
verificar a situação do aluno (aprovado ou reprovado)."""


class Aluno:
    def __init__(self, nome, notas):
        self.__nome = nome
        self.__notas = notas
        self.__situacao = None

    def get_nome(self):
        return self.__nome

    def get_notas(self):
        return self.__notas

    def media(self):
        soma = 0
        for notas in self.get_notas():
            soma += notas

        media = soma / len(self.get_notas())

        self.set_situacao(media)

        return media

    def get_situacao(self):
        return self.__situacao

    def set_situacao(self, media):
        if media >= 9.5:
            self.__situacao = 'Aprovado'
        else:
            self.__situacao = 'Reprovado'


notas = list()

for c in range(0, 5):
    nota = float(input('Digite a nota: '))
    notas.append(nota)

aluno = Aluno('Ricardo', notas)

print(aluno.get_nome())
print(aluno.media())
print(aluno.get_situacao())