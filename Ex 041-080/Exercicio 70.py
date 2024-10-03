"""Crie um programa que tenha uma função
chamada area() que receba as dimensões
de um terreno e mostre a área do
terreno. """

def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área do terreno de {largura}m de largura e {comprimento}m de comprimento é de {area_terreno}m².')

print("Controle de Terrenos")
print("-" * 30)
largura = float(input("Largura do terreno (m): "))
comprimento = float(input("Comprimento do terreno (m): "))

area(largura, comprimento)