'''Crie um programa que leia várias notas
introduzidas pelo utilizador. No final
mostre quantas notas o utilizador inseriu, qual a média entre elas e
qual a maior e a menor nota.'''

qtdNotas = 0
media = 0
maior = 0
menor = 0

while True:
    notas = float(input('Digite uma nota [999 para parar]: '))
    if notas == 999:
        break
    else:
        qtdNotas += 1
        media += notas

        if qtdNotas == 1:
            maior = notas
            menor = notas
        else:
            if notas > maior:
                maior = notas
            if notas < menor:
                menor = notas

media = media / qtdNotas

print(f'Digitou {qtdNotas} notas.')
print(f'A média é {media} valores')
print(f'A maior nota digitada foi {maior}')
print(f'A menor nota digitada foi {menor}')