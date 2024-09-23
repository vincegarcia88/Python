#Faça um programa que leia uma frase
#qualquer e diga se é um palíndromo,
#desconsiderando os espaços.

#Ex: Anotaram a data da maratona

frase = input("Digite uma frase: ").strip().lower()
frase = frase.replace(__old=" ", __new=" ")

fraseControle = frase [::-1]

print (f"A frase digitada foi {frase}.")
print (f"A frase digitada ao contrário foi {fraseControle}. ")

if frase == fraseControle:
    print ("A frase digitada é um palíndromo.")

else:
    print ("A frase digitada NÃO é um palíndromo.")