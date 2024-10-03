"""Crie um programa que tenha uma função que receba vários parâmetros como
valores inteiros. O programa deve analisar todos os valores e dizer qual
deles é o maior."""

def verifica_maior(*numeros):
    maior = None

    contador = 0
    for numero in numeros:
        if contador == 0:
            maior = numero
            contador += 1
        else:
            if numero > maior:
                maior = numero
            contador += 1
    print(f'O maior valor digitado foi: {maior}')


verifica_maior(1, 2, 3, 4, 5, 6)
verifica_maior(-1, 5, -41, 6, 7)
verifica_maior(6, 5486, 44949, 84, 984, 564, 6, 8494, 984)