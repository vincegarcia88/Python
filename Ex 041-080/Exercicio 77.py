
"""Crie um programa que tenha uma função que vai receber como parâmetro o ano de
nascimento de uma pessoa e que retorne se a pessoa já pode tirar a carta de
condução, se precisa de autorização do encarregado de educação ou se não pode.

+18 anos – pode
-16 anos – não pode
-18 e +16 – com autorização"""

def verificar_carta(ano_nascimento):
    from datetime import datetime

    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        return "Apto a tirar a carta de condução."

    elif 16 <= idade < 18:
        return "Precisa de autorização do responsável."

    else:
        return "Inapto a tirar a carta de condução."

ano_nascimento = int(input("Digite o ano de nascimento: "))
resultado = verificar_carta(ano_nascimento)
print(resultado)


#Versão do professor
"""def valida_carta(ano_nascimento):
    from datetime import datetime

    data = datetime.now()
    ano_atual = data.year

    idade = ano_atual - ano_nascimento

    if idade >= 18:
        return f'Com {idade} anos pode tirar a carta de condução.'
    elif idade < 16:
        return f'Com {idade} anos não pode tirar a carta de condução.'
    else:
        return f'Com {idade} anos pode tirar a carta de condução com autorização.'''


ano_de_nascimento = int(input('Digite o ano de nascimento: '))
print(valida_carta(ano_de_nascimento))"""