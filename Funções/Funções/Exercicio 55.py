'''Crie um programa que tenha um tuple com
nomes de jogos e os seus respetivos
preços em sequência.

No final, mostre uma listagem de preços
organizados como tabela.'''

lista = ('Stellar Blade PS5', 69.99,
         'Rise of The Ronin PS5', 69.99,
         'Marvels Spider-Man: Miles Morales PS5', 39.99,
         'God of War Ragnarok PS5', 59.99,
         'The Last of Us: Parte I (Em Português) PS5', 59.99)

tam = len(lista)

print('*'*60)
print(f'{'TABELA DE PREÇOS':^60}')
print('*'*60)
for indice in range(0, tam):
    if indice % 2 == 0:
        print(f'{lista[indice]:.<50}\t{lista[indice + 1]:>7}€')
print('*'*60)

