'''Crie um programa que leia um número de
0 a 20 introduzido pelo utilizador.
Depois deverá mostrar por extenso o
número introduzido.'''

numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez,'
           'onze','doze','treze','catorze','quinze','dezesseis','dezessete',
           'dezoito', 'dezenove','vinte')

while True:
    numero = int(input("Digite um número de 0 a 20: "))
    if numero < 0 or numero > 20:
        print("Digite um número VÁLIDO entre 0 e 20")
    else:
        break

print (f'{numero} -> {numeros[numero]}')