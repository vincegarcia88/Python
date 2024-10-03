#Crie um programa que leia uma
#frase e mostre:
#✓ Quantas vezes aparece a letra “A”;
#✓ Em que posição aparece a primeira vez;
#✓ Em que posição aparece a última vez.

name = input ("Escreva seu nome: ").upper()

#Quantas vezes aparece a letra A
print (name.count("A"))

#Em que posição aparece a primeira vez
print(name.find("A"))
print (f"Posição {name.find("A")}")

#Em que posição aparece a última vez
print (f"Aparece {name.rfind("A")+1}")