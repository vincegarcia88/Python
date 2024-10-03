'''Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando cada
dado num dicionário e todos os dicionários numa lista. No final mostre:

a) Quantas pessoas foram registadas;
b) Qual a média de idades do grupo;
c) Quantas mulheres foram registadas;
d) Quantos homens com idade acima da média foram
registados.'''

pessoas = list()

qtdPessoasRegistadas = 0
somaIdades = 0
qtdMulheresRegistadas = 0


while True:
    pessoa = dict()
    pessoa['nome'] = input('Digite o nome: ')
    while True:
        pessoa['sexo'] = input('Digite o sexo [M/F]: ').upper()
        if pessoa['sexo'] == 'M' or pessoa['sexo'] == 'F':
            break
    if pessoa['sexo'] == 'F':
        qtdMulheresRegistadas += 1

    pessoa['idade'] = int(input('Digite a idade: '))
    somaIdades += pessoa['idade']
    pessoas.append(pessoa.copy())
    opcao = input('Deseja continuar [S/N]: ')
    qtdPessoasRegistadas += 1
    if opcao == 'S':
        break

mediaIdades = somaIdades / qtdPessoasRegistadas


qtdHomensIdadeMaiorMedia = 0

for pessoa in pessoas:
    if pessoa['sexo'] == 'M' and pessoa['idade'] > mediaIdades:
        qtdHomensIdadeMaiorMedia += 1


print(f'Quantidade pessoas registadas: {qtdPessoasRegistadas}')
print(f'Média de Idades: {mediaIdades}')
print(f'Quantidade de mulheres registadas: {qtdMulheresRegistadas}')
print(f'Quantidade de homens com idade acima da média: {qtdHomensIdadeMaiorMedia}')