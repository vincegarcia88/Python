from time import sleep

print ("-="*11)
print ("Registro de colaborador")
print ("-=" *11)
print ("\n")
pnome = input ("Digite o seu primeiro nome: ")
unome = input ("Digite o seu sobrenome: ")

print ("Estamos a processar...")
sleep (2)

email = pnome[0]+"."+ unome.lower() + "edu@empresa.pt"
print(f"Olá {pnome}, o registro está completo.")

print (f"O seu email é: {email}")
