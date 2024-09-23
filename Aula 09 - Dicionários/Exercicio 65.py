'''Crie um programa que sorteie a ordem de jogada num jogo ao “atirar um dado ao
ar”. Cada jogador terá um número aleatório associado dentro de um
dicionário. No final ordene o ranking para ver a ordem de jogada.'''

import random

dado = random.randint (1,6)

ranking = list()
jogador = dict()

for c in range (0,4):
    jogador = dict()

    jogador["Nome"] = f"jogador {c+1}"
    jogador["Jogada"] = random.randint(1,6)

    #guarda dicionario jogador na lista ranking
    if c == 0:
        ranking.append (jogador.copy())
        continue

    if jogador ["Jogada"] >= ranking [-1] ["Jogada"]:
        ranking.append (jogador.copy())
        continue

    else:
        posicao = 0
        while posicao <= len(ranking):
            if jogador["Jogada"] <= ranking [posicao]["Jogada"]:
                ranking.insert(posicao, jogador.copy())
                break
            posicao += 1

#Resultado de forma ordenada
print ("--- ORDEM DE JOGADA---")
c = 0
tamanho = len(ranking)

for c in range (tamanho, 0, -1):
    if
    for k, v in ranking[c].items()]:

        print(f"{contador + 1}º -> {v}")
        contador += 1


        if k == "Jogada":
            continue

        else:
            print (f"{c+1}º -> {v}")

    c += 1

