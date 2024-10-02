def calcula_fatorial(numero, mostra=False):
    from math import factorial
    fatorial = factorial(numero)

    if not mostra:
        return f'A fatorial de {numero} é {fatorial}.'
    else:
        calculo_completo = list()
        inicio = str(numero) + ' x '
        calculo_completo.append(inicio)

        for c in range(numero - 1, 0, -1):
            if c == 1:
                fim = str(c) + ' = ' + str(fatorial)
                calculo_completo.append(fim)
            else:
                meio = str(c) + ' x '
                calculo_completo.append(meio)
        return calculo_completo


print('--- Calcula Fatorial ---')

numero = int(input('Digite o número para saber o seu fatorial: '))
opcao = int(input('1 - Mostrar cálculo\n2 - Não mostrar cálculo\n--> '))
if opcao == 1:
    opcao = True
else:
    opcao = False

fatorial_calculado = calcula_fatorial(numero, opcao)

if type(fatorial_calculado) == list:
    for letra in fatorial_calculado:
        print(f'{letra}', end='')
else:
    print(fatorial_calculado)