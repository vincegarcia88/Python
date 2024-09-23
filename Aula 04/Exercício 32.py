#Faça um programa que simule uma
#contagem regressiva para a passagem de
#ano, de 10 até 0, com 1 segundo de
#pausa entre eles.

from time import sleep

for c in range (10,0, -1):
    sleep (1)
    print (c)
print ("Feliz ano novo!")