#Cria um programa que leia um
#número introduzido pelo
#utilizador e que mostre o seu
#antecessor e sucessor.

num1 = int (input ("Insira um número: "))

#Calcular o antecessor e o sucessor
antecessor = num1 -1
sucessor = num1 +1

#Apresentar os resultados
print ("O número digitado foi" , num1)
print ("O antecessor do número introduzido é", antecessor, (".") )
print ("E o sucessor do número introduzido é", sucessor, ("."))