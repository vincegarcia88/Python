#Fatiamento de strings

#Fatia o caractere inserido abaixo
frase = "Curso de Python"
print (frase [9])

#Curso
print (frase[0:5])

#Do caractere 9 até 15
print(frase[9:15])

#Do caractere 9 ao 15, de 2 em 2
print(frase[9:15:2])

#Do 0 até o final de 3 em 3
print(frase[0::3])

#O LEN escaneia a frase inteira e a outra função trabalha
len(frase)
print (frase.count ("o"))

#contagem da letra O, do 0 ao 5
print (frase.count ("o",0,5))

#Qual o caractere numérico representa o T
print(frase.find ("t"))

#Procura se tem a palavra Curso dentro de frase
print ("curso" in frase)

#Substitui a primeira pela segunda
print (frase.replace ("Python", "C++"))

#Primeira letra maiúscula
print (frase.capitalize())

#Primeiras letras maiúsculas
print (frase.title())

#Corta espaços vazios
print (frase.strip())
print (frase.rstrip())
print (frase.lstrip())

#Separa as palavras em blocos
print (frase.split ())

#Separa adicionando caracteres nos espaços vazios
print ("_".join (frase)) #No caso aqui, um underscore