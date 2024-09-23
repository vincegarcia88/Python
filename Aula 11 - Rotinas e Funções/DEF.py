"""def insere_linha ():
    print("Lalalalala")

insere_linha()"""

#Tabuada
"""def cabecalho (titulo):
    print ("-----------TABUADA-----------")

def mostra_tabuada(numero):
    for c in range (0,10):
        print(f"{numero} x {c+1} = {numero* (c+1)}")

cabecalho ("TABUADA")
numero = int(input("Digite um numero: "))
mostra_tabuada(numero)
cabecalho ("Ate a proxima")"""


#Desempacotador (O asterisco em num recebe)
"""def contador(*num):
    for valor in num:
            print(f"{valor}", end="")
            print("Fim")

numeros = [1,2,3,4,5]
contador(numeros)"""

#Outro exemplo

def soma_numeros(num1, num2):
    soma = num1 + num2
    print(soma)

#programa principal
num1 =int(input("Digite um numero: ")
num2 = int(input("Digite outro numero: "))

soma_numeros()