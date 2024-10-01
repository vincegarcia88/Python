"""Crie um programa que tenha uma função que converta a temperatura de Celsius
para Fahrenheit."""

def conversao(temperatura):
    fahrenheit = temperatura * 1.8 + 32

    print(f"Em Celsius: {temperatura}Cº")
    print(f"Em Fahrenheit {fahrenheit}Fº")

    conversao(45)