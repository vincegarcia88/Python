'''Crie uma classe chamada Produto que inclua
atributos para o nome e a quantidade em
stock. Utilize a property para aceder a
quantidade em stock, garantindo que ela nunca
seja negativa. Inclua um método mostrar_stock
que exibe uma mensagem indicando quantas
unidades do produto estão disponíveis.
Adicione também um método adicionar_stock que
permite aumentar a quantidade de stock de um
produto.'''

class Produto:
    def __init__(self,nome,quantidade_stock = 0):
        self.__nome = nome
        self.__quantidade_stock = quantidade_stock
        
    @property
    def quantidade_stock(self):
        return self.__quantidade_stock
    
    @quantidade_stock.setter
    def quantidade_stock (self,quantidade):
        if quantidade >= 0:
            self.quantidade_stock = quantidade
        else: 
            print(f'O valor do stock não pode ser negativo.')

    def mostrar_stock(self):
        print(f"O produto '{self.__nome}' tem {self.__quantidade_stock} unidades em stock.")
        
    def adicionar_stock(self,quantidade):
        if quantidade > 0:
            self.__quantidade_stock += quantidade
            print(f"{quantidade} unidades foram adicionadas ao stock de '{self.__nome}'.")
        else:
            print("A quantidade a ser adicionada deve ser positiva.")


produto1 = Produto('banana',500)
produto1.mostrar_stock()

produto1.adicionar_stock(5)
produto1.mostrar_stock()

produto1.quantidade_stock = -2
produto1.mostrar_stock()





        



