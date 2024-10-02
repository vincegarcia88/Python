'''Desenvolva o jogo par ou ímpar. O jogo
só será interrompido quando o jogador
perder e deverá exibir o total de
vitórias consecutivas.'''

from random import randint

jogadaCPU = randint(0, 5)
qtdVitorias = 0

while True:
    print('--- PAR OU ÍMPAR ---')
    jogada = int(input('Escolha um número: '))

    print('[ 1 ] - PAR')
    print('[ 2 ] - ÍMPAR')
    escolha = int(input('--> '))

    soma = jogada + jogadaCPU

    if soma % 2 == 0:
        if escolha == 1:
            print('GANHOU!!')
            print(f'Eu escolhi {jogadaCPU} e você escolheu {jogada}')
            print(f'A soma deu {soma}, ou seja, PAR!')
            qtdVitorias += 1
        elif escolha == 2:
            print('PERDEU!!')
            print(f'Eu escolhi {jogadaCPU} e você escolheu {jogada}')
            print(f'A soma deu {soma}, ou seja, ÍMPAR!')
            break
    else:
        if escolha == 1:
            print('PERDEU!!')
            print(f'Eu escolhi {jogadaCPU} e você escolheu {jogada}')
            print(f'A soma deu {soma}, ou seja, ÍMPAR!')
            break
        elif escolha == 2:
            print('GANHOU!!')
            print(f'Eu escolhi {jogadaCPU} e você escolheu {jogada}')
            print(f'A soma deu {soma}, ou seja, PAR!')
            qtdVitorias += 1

print(f'Vitórias consecutivas: {qtdVitorias}')