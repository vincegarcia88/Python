#Crie um programa que leia o nome
#completo de uma pessoa e mostre:
#✓ O nome com todas as letras maiúsculas;
#✓ O nome com todas as letras minúsculas;
#✓ Quantidade de letras sem espaços;
#✓ Quantas letras tem o primeiro nome.

#Todas as letras maiúsculas
nome = input("Insira seu nome completo: ")
print (nome.upper())

#Todas as letras minúsculas
print (nome.lower())

#Quantidade de letras sem espaços
nome_sem_espaco = nome.replace("", "")
quantidade_de_letras = len(nome_sem_espaco)
print(quantidade_de_letras)

#Quantas letras tem o primeiro nome
nome = input("Insira o nome: ")
sobrenome = input ("Insira o sobrenome: ")
contagem_de_nome = len(nome)
print (contagem_de_nome)

nome = input("Digite o seu nome: ".strip)
print (f "Quantidade de letras sem espaço: {nome}{sobrenome}")
