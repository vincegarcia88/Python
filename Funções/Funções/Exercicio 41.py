#Desenvolva um programa que faça 3 perguntas ao utilizador
#e apenas aceite como resposta "V" ou "F". Caso esteja
#errado, peça para repetir a resposta até ter um valor correto.

pergunta = ("O céu é azul? [V/F]", "Ronaldo já foi o melhor do mundo? [V/F]" , "1 + 1 é 2? [V/F]")

resposta = ""

c = 1

while resposta != "v":
    print("O céu é azul? [V/F]")
    resposta = input("Resposta: -> ").strip().lower()

    if resposta!= "v" and resposta !="f":
        print("Resposta inválida.")

    elif resposta == "f":
        print("Errado. Tente novamente...")

print("Acertou!")
resposta = ""


while resposta != "v":
    print("Ronaldo já foi o melhor do mundo? [V/F]")
    resposta = input("Resposta: -> ").strip().lower()
    if resposta!= "v" and resposta !="f":
        print("Resposta inválida.")
    elif resposta == "f":
        print("Errado. Tente novamente...")

print("Acertou!")
resposta = ""

while resposta != "f":
    print("Ronaldo já foi o melhor do mundo? [V/F]")
    resposta = input("Resposta: -> ").strip().lower()
    if resposta!= "f" and resposta !="v":
        print("Resposta inválida.")
    elif resposta == "v":
        print("Errado. Tente novamente...")

print("Parabéns! ")

#
'''from time import sleep

resposta = ''

while resposta != 'v':
    print("O céu é azul?")
    resposta = input('[V / F] ->').strip().lower()
    if resposta != 'v' and resposta != 'f':
        print('Resposta inválida.')
    elif resposta == 'f':
        print('Errado. Tente novamente...')
    sleep(1)

print("Acertou!!!")
resposta = ''

while resposta != 'v':
    print("Temos livre arbitrio?")
    resposta = input('[V / F] ->').strip().lower()
    if resposta != 'v' and resposta != 'f':
        print('Resposta inválida.')
    elif resposta == 'f':
        print('Errado. Tente novamente...')
    sleep(1)

print('Acertou!!!')
resposta = ''

while resposta != 'v':
    print("Está a chover?")
    resposta = input('[V / F] ->').strip().lower()
    if resposta != 'v' and resposta != 'f':
        print('Resposta inválida.')
    elif resposta == 'f':
        print('Errado. Tente novamente...')
    sleep(1)

print('Acertou!!!')

print('Programa terminado!')'''