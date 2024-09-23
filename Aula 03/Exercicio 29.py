#Crie o seguinte menu:

#--- Calculadora ---
#[ 1 ] – Tabuada
#[ 2 ] – Calculadora
#[ 3 ] – Números Pares
#[ 4 ] – Sair

#Mediante a opção solicitada o sistema
#deve executar a ação do menu.

print ("-----MENU-----")
print ("[1] - Calculadora")
print ("[2] - Tabuada")
print ("[3] - Pares")
print ("[4] - Sair")

opcao = int (input("---->"))

if opcao == 1:
    print("----CALCULADORA----")
    num1 = int(input ("Número: "))
    operacao = input("Operação: ")
    num2 = int(input("Número: "))

    if operacao == "+":
        print(f"{num1}+{num2} = {num1 + num2}")

    elif operacao == "-":
        print(f"{num1}-{num2} = {num1 - num2}")

    elif operacao == "x":
        print(f"{num1}*{num2} = {num1 * num2}")

    elif operacao == "/":
        print(f"{num1}/{num2} = {num1 / num2}")
            if num2 == 0:
                print ("Não é possível dividir por 0.")

            else:
                print(f"{num1}/{num2} = {num1 / num2}")