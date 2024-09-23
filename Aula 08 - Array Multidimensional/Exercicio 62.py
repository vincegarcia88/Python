'''Melhore o exercício 61, exibindo no final.

a) A soma de todos os valores pares.
b) A soma dos valores da segunda coluna.
c) O maior valor da terceira linha.'''

matriz = list()

#Primeiro FOR roda 3x e só passa para o seguinte
#quando o FOR interno terminar

for linha in range(0, 3):
    numeros = list()
    for coluna in range(0, 3):
        numero = int(input(f'Digite um número para a linha {linha} coluna {coluna}: '))
        numeros.append(numero)
    matriz.append(numeros)

print("\nMatriz:")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]}', end='\t')
    print()

# Soma de todos os valores pares
soma_pares = 0
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            soma_pares += numero

# Soma dos valores da segunda coluna (índice 1)
soma_segunda_coluna = 0
for linha in range(0, 3):
    soma_segunda_coluna += matriz[linha][1]

# Maior valor da terceira linha (índice 2)
maior_terceira_linha = 0
for linha in range (0,3):
    maior_terceira_linha = matriz[linha][2]

# Exibir os resultados
print(f"\nA soma de todos os valores pares é: {soma_pares}")
print(f"A soma dos valores da segunda coluna é: {soma_segunda_coluna}")
print(f"O maior valor da terceira linha é: {maior_terceira_linha}")
