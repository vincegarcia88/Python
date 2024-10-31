"""Adicione um método à classe desenvolvida no exercício anterior Livro que imprime
uma descrição do livro no formato:

“O livro com o titulo X foi escrito pelo autor Y"."""

import os

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
        print(f"O livro com o título '{self.titulo}' foi escrito pelo autor '{self.autor}'.")


# Instanciando três objetos da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")
livro3 = Livro("A Revolução dos Bichos", "George Orwell")

# Imprimindo a descrição dos livros
livro1.descricao()
livro2.descricao()
livro3.descricao()

        