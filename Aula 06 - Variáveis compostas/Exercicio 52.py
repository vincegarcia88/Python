'''Crie um programa com um tuple com os 20
primeiros classificados do Campeonato
Espanhol de Futebol. Depois mostre:

a) Os primeiros 5 classificados.
b) Os últimos 4 classificados.
c) Uma lista com as equipas por ordem alfabética.
d) A posição da equipa Las Palmas.'''


listaEquipas = (
'Real Madrid',
'Barcelona',
'Atlético de Madrid',
'Girona',
'Alavés',
'Athletic',
'Bilbao',
'Betis',
'Celta',
'Espanyol',
'Getafe',
'Las Palmas',
'Leganés',
'Mallorca',
'Osasuna',
'Rayo Vallecano',
'Real Sociedad',
'Sevilla',
'Valencia',
'Valladolid',
'Villarreal')

primeirosCinco = (listaEquipas [0:5])
print (f"Primeiros 5 classificads:\n{primeirosCinco}")

ultimosQuatro = (listaEquipas[-1:-5])
print (f"Últimos 4 classificados:\n{ultimosQuatro}\n")

print (f"Lista por ordem alfabética:\n{sorted listaEquipas}\n")
'''corrigir'''

ultimosQuatro = (listaEquipas [-4::])
'''[:15:-1]) Ou esse mais dificil'''
print(ultimosQuatro)

indice = 0
for elemento in listaEquipas:
    if elemento == "Las Palmas":
        break
    indice += 1
print(f"Las Palmas está em {indice +1}classificado")
