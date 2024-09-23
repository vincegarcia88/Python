#Cria um programa que leia 2
#valores introduzidos pelo
#utilizador e que apresente a
#sua SOMA, SUBTRAÇÃO,
#MULTIPLICAÇÃO, DIVISÃO e RESTO.

#Ler as entradas
num1 = int (input ("Insira um número: "))
num2 = int (input ("Insira outro número: "))

#Calcular os resultados
soma = num1 + num2
subtracao = num1-num2
multiplicacao = num1*num2
divisao = num1/num2
resto = num1%num2

#Apresentar os resultados
print ("A soma dos números inseridos é", soma,".")
print ("A subtração é", subtracao,".")
print ("A multiplicação dos valores é", multiplicacao,".")
print ("A divisão é", divisao,".")
print ("O resto é de", resto,".")
