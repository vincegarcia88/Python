'''Tabuada V2.0 – Faça um programa que
mostre a tabuada de vários números
inseridos pelo utilizador.

O programa deverá ser interrompido quando o
número inserido for negativo ou 0.'''

while True:
    print ("---Tabuada 2.0---")
    numero = int(input("Digite um número para saber a sua tabuada: "))
    if numero < 1:
        print ("Xaaau!")
        break

    else:
        contador = 1
        while contador < 11:
            print(f'{numero} x {contador} = {numero * contador}')
            contador+= 1
        print ('\n\n')
        break

