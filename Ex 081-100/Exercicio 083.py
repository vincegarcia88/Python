"""Escreva um programa que peça ao utilizador para inserir dois números e
divida o primeiro pelo segundo.

Utilize o tratamento de exceções para lidar com casos em que o segundo número é zero e
quando a entrada não é um número válido."""

while True:
    try:
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
        divisao = numero1 / numero2

    except ZeroDivisionError:
        print('Não é possível dividir por ZERO')

    except ValueError:
        print('Por favor insira números válidos.')

    except KeyboardInterrupt:
        print('Por favor digite os números.')

    else:
        print(divisao)
        print('Xau e adeus.')
        break