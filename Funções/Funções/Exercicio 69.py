'''Melhore o exercício 67 para que permita a entrada de vários jogadores. Defina um
sistema de visualização que permita ao utilizar procurar pelos resultados de um
jogador específico.'''


jogadores = list()

while True:
    jogador = dict()

    jogador['Nome'] = input('Digite o nome do Jogador: ')
    jogador['Golos'] = int(input('Digite a quantidade de golos: '))
    jogador['Jogos'] = int(input('Digite a quantidade de jogos: '))
    jogador['Média'] = jogador['Golos'] / jogador['Jogos']

    jogadores.append(jogador.copy())

    opcao = input('Deseja continuar [S/N]: ').strip().upper()
    if opcao == 'N':
        break

while True:
    opcao = input('Qual jogador deseja ver: [999 para sair]')
    if opcao == '999':
        break

    for jogador in jogadores:
        if jogador['Nome'] == opcao:
            for k, v in jogador.items():
                print(f'{k} -> {v}')
                break
        else:
            print('Jogador não encontrado...')