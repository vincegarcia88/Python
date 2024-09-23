contador = 1

#while contador < 2:
 #   print (contador)
#    contador -= 1

# =-=-=-=-=-=-=-=-=-

contadorPessoas = 0

opcao = input("Já entrou toda a gente? [S / N]").strip().lower()

print (f"Entraram {contadorPessoas} pessoas.")

#=-=-=-=-=-=-=-

contadorPessoas = 0

while True:
    opcao = input ("Entrou alguém: [S/N]").strip().lower()

    if opcao == "n":
        break #um ponto para parar a contagem
        continue #ignora o restante e volta pra cima
print ("Saí do programa")



