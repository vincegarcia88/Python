'''Crie um simulador de crédito habitação simples e sem taxas, que solicite o nome,
ano de nascimento, rendimentos mensais, despesas mensais, montante do crédito e
prazo em anos, guardando tudo dentro de um dicionário.

Calcule, acrescentando ao dicionário, a idade, o remanescente após
despesas, quanto deverá pagar mensalmente pelo crédito e se o crédito foi aprovado
sempre que o remanescente seja superior ao valor mensal do crédito.'''

from time import sleep
from datetime import datetime

dados = dict()

print('--- SIMULADOR DE CRÉDITO HABITAÇÃO ---\n')
print('A carregar', end='')
for c in range(0, 3):
    sleep(1)
    print('.', end='')
print()

dados['nome'] = input('Nome: ')
dados['ano de nascimento'] = int(input('Ano de Nascimento: '))
dados['rendimentos mensais'] = float(input('Redimentos mensais: '))
dados['despesas mensais'] = float(input('Despesas mensais: '))
dados['montante do crédito'] = float(input('Montante do Crédito: '))
dados['prazo em anos'] = int(input('Prazo: '))

data = datetime.now()
ano = data.year

dados['idade'] = ano - dados['ano de nascimento']
dados['remanescente'] = dados['rendimentos mensais'] - dados['despesas mensais']
dados['prestação mensal'] = dados['montante do crédito'] / (dados['prazo em anos'] * 12)
dados['estado'] = 'Aprovado' if dados['remanescente'] > dados['prestação mensal'] else 'Reprovado'

for k, v in dados.items():
    if type(v) == float:
        print(f'{k} -> {round(v)}€')
    else:
        print(f'{k} -> {v}')
    sleep(1)

