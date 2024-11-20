"""Desenvolva um programa que permita ao utilizador
calcular o seu Índice de Massa Corporal (IMC).

O programa deve solicitar ao utilizador a sua altura e
o seu peso. De seguida, utilizando uma função, deve calcular o IMC e o programa deve exibir uma mensagem
com base no valor do IMC calculado.

● IMC abaixo de 18,5: Abaixo do peso
● IMC entre 18,5 e 24,9: Peso normal
● IMC entre 25,0 e 29,9: Sobrepeso
● IMC entre 30,0 e 34,9: Obesidade grau 1
● IMC entre 35,0 e 39,9: Obesidade grau 2
● IMC acima de 40,0: Obesidade grau 3 (obesidade mórbida)"""

def mostra_imc(altura_metros, peso_kg):
    imc = peso_kg / (altura_metros * altura_metros)

    if imc < 18.5:
        return f'IMC: {round(imc, 1)} -> Abaixo do peso'
    elif 18.5 <= imc < 24.9:
        return f'IMC: {round(imc, 1)} -> Peso normal'
    elif 25 <= imc < 29.9:
        return f'IMC: {round(imc, 1)} -> Sobrepeso'
    elif 30 <= imc < 34.9:
        return f'IMC: {round(imc, 1)} -> Obesidade grau 1'
    elif 35 <= imc < 39.9:
        return f'IMC: {round(imc, 1)} -> Obesidade grau 2'
    elif imc >= 40:
        return f'IMC: {round(imc, 1)} -> Obesidade grau 3 (obesidade mórbida)'


altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite o seu peso: '))

print(mostra_imc(altura, peso))



