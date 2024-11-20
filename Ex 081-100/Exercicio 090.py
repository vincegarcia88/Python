"""Crie uma classe chamada Livro que tenha dois atributos: titulo e autor.
Instancie três objetos dessa classe e imprima os valores dos atributos."""

import os

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Instanciando três objetos da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")
livro3 = Livro("A Revolução dos Bichos", "George Orwell")

# Imprimindo os valores dos atributos
print(f"Título: {livro1.titulo}, Autor: {livro1.autor}")
print(f"Título: {livro2.titulo}, Autor: {livro2.autor}")
print(f"Título: {livro3.titulo}, Autor: {livro3.autor}")


        