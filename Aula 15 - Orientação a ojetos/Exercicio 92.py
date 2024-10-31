"""Crie uma classe Produto com os atributos nome e quantidade em stock. 
Adicione um método que mostre o stock no estilo “O
produto X tem Y unidades em stock”.

Adicione um novo método que aumenta a quantidade de stock numa determinada
quantidade."""

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    
    def mostra_stock(self):
        print(f"O produto{self.nome} tem {self.quantidade} unidades em stock.")

    def aumenta_stock (self, valor):
        self.quantidade += valor
    
cenouras = Produto (" Cenouras", 50)
batatas = Produto(" Batatas", 25)
cebolas = Produto (" Cebolas", 75)

cenouras.mostra_stock()
cenouras.aumenta_stock(10)
cenouras.mostra_stock()