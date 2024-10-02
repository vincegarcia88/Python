'''Crie um programa que leia a idade e o
sexo de várias pessoas. A cada pessoa
registada o programa deverá perguntar
se o utilizador quer continuar ou não.
No final mostre:

a) Quantas pessoas têm mais de 25 anos.
b) Quantos homens com menos 17 anos foram
registados.
c) Quantas mulheres foram registadas.
d) Quantos menores de idade foram registados.'''

qtdMais25 = 0
qtdHomensMenos17 = 0
qtdMulheres = 0
qtdMenores18 = 0
opcao = ''

print('--- REGISTO ---')


while opcao != 'n':
    idade = int(input('Digite uma idade: '))
    if idade < 0:
        print('Idade inválida.')
        continue

    sexo = input('Digite o sexo [M / F]: ').strip().lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo inválido!')
        continue

    if idade < 18:
        qtdMenores18 += 1
    if idade > 25:
        qtdMais25 += 1
    if sexo == 'f':
        qtdMulheres += 1
    if sexo == 'm' and idade < 17:
        qtdHomensMenos17 += 1

    opcao = input('Quer continuar? [S / N]: ').strip().lower()

    while opcao != 's' and opcao != 'n':
        print('Opção inválida')
        opcao = input('Quer continuar? [S / N]: ').strip().lower()

print(f'Quantidade de Pessoas com +25 anos: {qtdMais25}')
print(f'Quantidade de Homens com -17 anos: {qtdHomensMenos17}')
print(f'Quantidade de Mulheres registadas: {qtdMulheres}')
print(f'Quantidade de Menores de idade registados: {qtdMenores18}')