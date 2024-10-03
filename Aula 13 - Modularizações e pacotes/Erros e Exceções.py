try:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    divisao = num1 / num2

#Dentro de um try se pode ter vários except
except Exception as erro:

    print (f"Erro por {erro}.")

except ZeroDivisionError:
    print(f"Não pode dividir por zero")

except ValueError:
    print(f"Erro na introdução de valores")

except KeyboardInterrupt:
    print(f"O utilizador preferiu sair do programa")

else:
    print("Divisão.")

finally:
    print("Programa terminado.")