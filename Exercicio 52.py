'''Crie um programa com um tuple com os 20
primeiros classificados do Campeonato
Espanhol de Futebol. Depois mostre:

a) Os primeiros 5 classificados.
b) Os últimos 4 classificados.
c) Uma lista com as equipas por ordem alfabética.
d) A posição da equipa Las Palmas.'''


# Lista das equipas
listaEquipas = ('Real Madrid',
                'Barcelona',
                'Girona',
                'Atlético Madrid',
                'Athletic Club',
                'Real Sociedad',
                'Real Betis',
                'Villarreal',
                'Valencia',
                'Deportivo Alavés',
                'Osasuna',
                'Getafe',
                'Celta de Vigo',
                'Sevilla',
                'Mallorca',
                'Las Palmas',
                'Rayo Vallecano',
                'Cádiz',
                'Almería',
                'Granada')

primeirosCinco = (listaEquipas[0:5])
print(f'Primeiros 5 classificados:\n{primeirosCinco}\n')
ultimosQuatro = (listaEquipas[-4::])
print(f'Últimos 4 classificados:\n{ultimosQuatro}\n')
print(f'Lista por ordem alfabética:\n{sorted(listaEquipas)}\n')

indice = 0
for elemento in listaEquipas:
    if elemento == 'Las Palmas':
        break
    indice += 1

print(f'Las Palmas está em {indice+1} classificado')