'''Desenvolva um programa que simule uma calculadora interativa
com diferentes funcionalidades. O programa deve exibir um
menu com várias opções e permitir que o utilizador escolha
uma das opções. O programa deve executar a funcionalidade
escolhida e quando terminar deve voltar a apresentar o menu.
Use o tratamento de exceções para lidar com entradas
inválidas (como strings ou caracteres) e erros matemáticos
(como divisão por zero). Todas as funções devem estar num
módulo bem estruturado e documentado.
Função- Calculadora [SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO]
Função- Tabuada
Função- Par ou Ímpar
Função- Números primos
Função- Factorial'''

def Calculadora(N1, N2):
    soma = N1 + N2
    subtracao = N1 - N2
    multiplicacao = N1 * N2
    divisao = N1 / N2
    print(f'Soma:{N1} + {N2} = {soma}')
    print(f'Subtracao:{N1} - {N2} = {subtracao}')
    print(f'Multiplicacao:{N1} * {N2} = {multiplicacao}')
    print(f'Divisao: {N1} / {N2} = {divisao}')

def tabuada(numero):
    for c in range(10):
        print(f'{numero} x {c + 1} = {numero * (c + 1)}')

def verificar_par_impar(numero):
    if numero % 2 == 0:
        print(f'O numero que inseriu é par')
    else:
        print(f'O numero que inseriu é impar')

def verificar_numero_primo(numeros_primos):
    for j in range(2, numeros_primos):
        # Assumimos que o número é primo
        primo = True
        for i in range(2, int(j ** 0.5) + 1):  # Verifica divisores de 2 até a raiz quadrada de j
            if j % i == 0:
                primo = False
                break
        if primo:
            print(j, 'é primo')
        else:
            print(j, 'não é primo')
def verificar_fatorial(fatorial):
    resultado = 1
    for c in range(fatorial, 1, -1):
        resultado = resultado * c
        print(c, ' * ', end='')
    print('1 = ', resultado)
    return resultado

#Mostrar Menu principal:Calculadora
while True:
    print('-=-=-=-Calculadora-=-=-=-')
    print('-=-=-=-Menu-=-=-=-')
    print('1.Calculadora')
    print('2.Tabuada')
    print('3.Par ou Impar')
    print('4.Números Primos')
    print('5.Fatorial')

    try:
        #Pedir ao utilizador para escolher uma das opções acima
        opcao = int(input('Digite uma das seguintes opções: '))

        if opcao == 1:
            N1 = int(input('Digite o primeiro numero: '))
            N2 = int(input('Digite o segundo numero: '))
            Calculadora(N1, N2)
        elif opcao == 2:
            numero = int(input('Tabuada do Numero: '))
            tabuada(numero)
        elif opcao == 3:
            numero = int(input('Digite um numero para verificar se é par ou impar: '))
            verificar_par_impar(numero)
        elif opcao == 4:
            numeros_primos = int(input('Quantos numeros primos pretende ver? '))
            verificar_numero_primo(numeros_primos)
        elif opcao == 5:
            fatorial = int(input('Fatorial do Número: '))
            resultado = verificar_fatorial(fatorial)
            print(f'Fatorial do numero {fatorial}: {resultado}')
    #Entradas inválidas (como strings ou caracteres)
    except ValueError:
        print(f'Erro na introdução de valores')
    #Erros Matemáticos
    except ZeroDivisionError:
        print(f'Não pode dividir por zero')