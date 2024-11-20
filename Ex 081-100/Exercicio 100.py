'''Desenvolva uma classe Temperatura que
armazene a temperatura em graus Celsius como
um atributo privado. Implemente um getter e
um setter usando property para permitir que a
temperatura seja ajustada e lida em Celsius,
e adicione métodos para converter a
temperatura para Fahrenheit e Kelvin.'''

class Temperatura:
    def __init__(self, celsius=0):
        self.__celsius = celsius  # Atributo privado para armazenar a temperatura em Celsius

    # Getter para a temperatura em Celsius
    @property
    def celsius(self):
        return self.__celsius

    # Setter para a temperatura em Celsius
    @celsius.setter
    def celsius(self, valor):
        self.__celsius = valor

    # Método para converter Celsius para Fahrenheit
    def converter_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    # Método para converter Celsius para Kelvin
    def converter_kelvin(self):
        return self.__celsius + 273.15

# Exemplo de uso
temp = Temperatura(25)  # Temperatura inicial de 25 °C

# Acessando a temperatura em Celsius
print(f"Temperatura em Celsius: {temp.celsius} °C")

# Convertendo para Fahrenheit
print(f"Temperatura em Fahrenheit: {temp.converter_fahrenheit()} °F")

# Convertendo para Kelvin
print(f"Temperatura em Kelvin: {temp.converter_kelvin()} K")

# Ajustando a temperatura e convertendo novamente
temp.celsius = 100
print(f"\nNova temperatura em Celsius: {temp.celsius} °C")
print(f"Temperatura em Fahrenheit: {temp.converter_fahrenheit()} °F")
print(f"Temperatura em Kelvin: {temp.converter_kelvin()} K")


