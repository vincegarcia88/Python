'''Crie o jogo da adivinha v2.0. O
computador deve “pensar” num número de
0 a 10 e o utilizador deve adivinhar o
número escolhido. Só que agora o jogador vai tentar adivinhar até
acertar. No final mostre quantas tentativas foram necessárias.'''

from random import randint

aleatorio = randint(0, 10)
tentativas = 0

opcao = 50
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('=-=- JOGO DA ADIVINHA -=-=-')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('\nPensei num número entre 0 e 10...\nSerá que consegues adivinhar?')

while opcao != aleatorio:
    opcao = int(input('Palpite: '))
    tentativas += 1
    '''
    - - Apenas para fazer um print na resposta errada - -
    if opcao != aleatorio:
        print('Errado... tente novamente.')
        '''
    if opcao > aleatorio:
        print('Mais abaixo...')
    elif opcao < aleatorio:
        print('Mais acima...')

print('PARABÉNS!!! ACERTOU!!!')
print(f'Eu escolhi o {aleatorio} e você o {opcao}')
print(f'Acertou em {tentativas} tentivas.')