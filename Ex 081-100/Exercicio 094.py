"""Crie uma classe chamada “Círculo” que possua um atributo privado para
armazenar o raio e métodos getters e setters para definir o raio, calcular a
área e o perímetro do círculo."""


class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    def get_raio(self):
        return self.__raio

    def set_raio(self, novo_raio):
        self.__raio = novo_raio

    def area(self):
        from math import pi
        return pi * (self.get_raio() ** 2)

    def perimetro(self):
        from math import pi
        return 2 * pi * self.get_raio()


novo_circulo = Circulo(2)
outro_circulo = Circulo(4)
ainda_outro_circulo = Circulo(1.75)

print(f'{ainda_outro_circulo.area():.2f}')
print(f'{ainda_outro_circulo.perimetro():.2f}')
