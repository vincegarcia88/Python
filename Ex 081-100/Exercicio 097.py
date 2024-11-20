"""Crie uma classe chamada Livro que tenha os atributos:
titulo, ano, autor e disponibilidade.
Utilize getters e setters para manipular as propriedades."""

class Livro:
    def __init__(self, titulo, ano, autor, disponibilidade=True):
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor
        self.__disponibilidade = disponibilidade

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter (self, novo_titulo):
        self.__titulo = novo_titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter (self, novo_ano):
        return self.__novo_ano

    @property
    def autor(self):
        return self.__autor

    @autor.setter(self, novo_autor):
        return self.__novo_autor

    @property
    def disponibilidade(self):
        return self.__disponibilidade

    @disponibilidade.setter (self, nada):
        if self.__disponibilidade:
            self.__disponibilidade = False

        else:
            self.__disponibilidade = True

livro =

    def __str__(self):
        return f"Livro: {self.__titulo}, Ano: {self.__ano}, Autor: {self.__autor}, Disponibilidade: {'Disponível' if self.__disponibilidade else 'Indisponível'}"

if __name__ == "__main__":
    livro = Livro("1984", 1949, "George Orwell")
    print(livro)

    livro.set_titulo("Animal Farm")
    livro.set_ano(1945)
    livro.set_autor("George Orwell")
    livro.set_disponibilidade(False)

    print(livro)
