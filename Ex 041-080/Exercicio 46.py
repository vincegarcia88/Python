#Crie um programa que leia vários números inteiros e que
#termine

qtdNumeros = 0
soma = 0

#Condição de saída = ZERO
while True:
    numero = int(input("Digite um número: [0000 para parar] "))
    if numero < 0:
        break
    else:
        qtdNumeros += 1
        soma += numero

print(f"Foram digitados {qtdNumeros} números.")
print(f"A soma dos números é {soma}.")
