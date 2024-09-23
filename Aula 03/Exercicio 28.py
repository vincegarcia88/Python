#Crie o jogo da adivinha v1.0. O
#computador deve “pensar” num número de
#0 a 7 e o utilizador deve adivinhar o
#número escolhido. O programa deve
#apresentar se o utilizador venceu ou
#perdeu.
#_____________________________________________
#Importar a biblioteca de números aleatórios
#Desta forma importo apenas randint, da biblioteca random

from random import randint
from time import sleep

#Gerar número aleatório
numero = randint (a:0,b:7)

print ("-=-=-=-=-=-=-=-=-=-=-=-=")
sleep (1)
print ("-=-=JOGO DA ADIVINHA-=-=")
sleep (1)
print ("-=-=-=-=-v.1.0-=-=-=-=-=")
sleep (1)
sleep (1)

print ("Pensei num múmero de 0 a 7...\nTenta adivinhar!!")
opcao = int (input ("Digite a sua escolha: "))

print("Vamos verificar!")
sleep (1)

if opcao == numero:
    sleep (1)
    print("Parabéns! Ganhou!")

else:
    sleep (1)
    print("Perdeu playboy! ERROU!!!")
