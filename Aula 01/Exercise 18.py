#Crie um programa que pergunte a
#quantidade de kms percorridos por um
#carro alugado e quantidade de dias que
#foi alugado. Apresente o total a pagar
#sabendo que o carro custa 60€/dia e
#0.456€/km.

#Definir variáveis
kmsPercorridos = float (input("Insira a quantidade de kms percorridos: "))
diasAlugados = float (input("Insira o número de dias de aluguel: "))
custo = 60.0
km = 0.456

#Cabeçalho
total_a_pagar = (diasAlugados * custo) + (kmsPercorridos * km)

print("O custo total a pagar é de",total_a_pagar,"euros.")