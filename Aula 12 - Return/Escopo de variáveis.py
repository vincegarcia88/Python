def mostra_valor():
    num1 = 7
    num1 += 5
    print(f'Na função vale: {num1}')


# Programa Principal
num1 = 10
print(f'Fora da função vale: {num1}')
mostra_valor()
print(f'Fora da função vale: {num1}')