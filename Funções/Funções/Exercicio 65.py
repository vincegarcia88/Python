'''Crie um programa que sorteie a ordem de jogada num jogo ao “atirar um dado ao
ar”. Cada jogador terá um número aleatório associado dentro de um
dicionário. No final ordene o ranking para ver a ordem de jogada.'''
import random  # Importa a biblioteca random para gerar números aleatórios.

# Cria uma lista vazia que vai armazenar os jogadores e suas jogadas ordenadas.
ranking = list()

# Este laço for repete 4 vezes, uma para cada jogador.
for c in range(0, 4):
    jogador = dict()  # Cria um dicionário vazio que irá armazenar as informações de cada jogador.

    # Atribui um nome para o jogador baseado no índice do laço (Jogador1, Jogador2, etc.).
    jogador['Nome'] = f'Jogador{c+1}'

    # Gera um número aleatório entre 1 e 6, simulando o "lançar de um dado".
    jogador['Jogada'] = random.randint(1, 6)

    # Se for o primeiro jogador (c == 0), adiciona diretamente ao ranking, já que não há com quem comparar.
    if c == 0:
        ranking.append(jogador.copy())  # O método copy() cria uma cópia do dicionário do jogador.
        continue  # Pula o resto do código e volta ao próximo ciclo do laço.

    # Se a jogada do jogador atual for maior ou igual à última jogada no ranking,
    # o jogador é adicionado ao final da lista.
    if jogador['Jogada'] >= ranking[-1]['Jogada']:
        ranking.append(jogador.copy())
        continue  # Volta ao próximo ciclo do laço.

    else:
        posicao = 0  # Inicializa a variável 'posicao' para começar a verificar a lista desde o início.

        # Este laço while percorre a lista ranking para encontrar a posição correta do jogador.
        while posicao <= len(ranking):
            # Se a jogada do jogador atual for menor ou igual à jogada em 'posicao' da lista,
            # insere o jogador nessa posição.
            if jogador['Jogada'] <= ranking[posicao]['Jogada']:
                ranking.insert(posicao, jogador.copy())  # Insere o jogador na posição encontrada.
                break  # Sai do laço while, pois o jogador já foi inserido.
            posicao += 1  # Incrementa a posição para continuar a busca.

# Imprime o ranking final dos jogadores com as suas jogadas, já ordenado.
print('--- ORDEM DE JOGADA ---')

contador = 1

# reversed itera de trás para a frente
for jogador in reversed(ranking):
    print(f'{contador}º -> {jogador["Nome"]} com {jogador["Jogada"]}')
    contador += 1