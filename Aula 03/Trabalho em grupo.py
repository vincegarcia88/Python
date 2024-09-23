print("Bem vindo à nossa aplicação!")

#Solicitar nome, email e password/ Registo do utilizador
print("Por favor inicie o seu registo:")
username = input("Insira um username: ")
email = input("Insira o seu email: ")
password = int(input("Insira uma password: "))
print("O seu registo foi executado com sucesso.")
print("")

#Opções
print("----MENU----")
print("[1] - Login")
print("[2] - Sair")
print("")
opcao = int(input("Escolha uma opção: "))
print("")

#Primeiro Login
if opcao == 1:
    login = input("Digite o seu login: ")
    password_login = int(input("Digite a sua password: "))

if login == username and password_login == password:
    print("Login correto.\n")
    print(f"Seja bem-vindo(a), {username}.")

#Segunda tentativa de login

elif opcao == 1:
    print ("Login incorreto.")
    print("")
    print("Tente novamente!")
    print("")
    login = input("Digite o seu login: ")
    password_login = int(input("Digite a sua password: "))

#Mensagem de bloqueamento e termino de conta
elif opcao == 1:
        login = input("Digite o seu login: ")
        password_login = int(input("Digite a sua password: "))

if login == username and password_login == password:
    print("")
    print("Prossiga")

else:
    print("Login incorreto.")
    print("")
    print("A sua conta encontra-se bloqueada e será terminada.")

#Mensagem de despedida da aplicação
if opcao == 2:
    login = input("Digite o seu login: ")
    password_login = int(input("Digite a sua password: "))
    print("")
    print ("Adeus! Até à próxima!")