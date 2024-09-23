'''Cria um programa que crie palpites para o Euromilhões.
O programa deve perguntar quantas chaves serão geradas
e deve sortear aleatoriamente 5 números de 1 a 50 [sem repetir] e 2 estrelas de
1 a 12 [sem repetir]. Cada sorteio deve ser guardado numa lista composta.'''

from random import randint

palpites = list()
estrelas = list()
numeros = list ()
palpite = list ()
numeroPalpites = int(input("Digite quantos palpites quer: "))

for c in range (0, numeroPalpites):
    while True:
        numero = randint (1,50)
        if len(estrelas) < 2:
            estrela = randint (1,12)
            if estrela in estrelas:
                continue

        else:
            estrelas.append(estrela)

        if numero in numeros:
            continue

        else:
            numeros.append(numero)

    if len(numeros) == 5 and len (estrelas) == 2:
        palpite.append (numeros[:])
        palpite.append (estrelas[:])
        numeros.clear()
        estrelas.clear()
        palpites.append(palpite [:])
        palpite.clear()

        print (palpite)
        break





