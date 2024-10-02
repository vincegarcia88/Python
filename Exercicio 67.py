'''Crie um programa que guarde o aproveitamento de um jogador de
futebol. O programa deverá ler o nome, quantos jogos jogou e a quantidade de
golos por jogo e guardar tudo num dicionário. No dicionário, deve
calcular a média de golos por jogo.'''

jogador = dict()

jogador['Nome'] = input('Digite o nome do Jogador: ')
jogador['Golos'] = int(input('Digite a quantidade de golos: '))
jogador['Jogos'] = int(input('Digite a quantidade de jogos: '))
jogador['Média'] = jogador['Golos'] / jogador['Jogos']

for k, v in jogador.items():
    print(f'{k} -> {v}')