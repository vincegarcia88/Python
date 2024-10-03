"""Crie um sistema que utilize o interactive help do python.
O utilizador deve digitar o comando e o sistema deve retornar o manual.
Quando o utilizador digitar “FIM” o programa deve encerrar."""

def ajuda(funcao):
    print(help(funcao))


opcao = None
while True:
    funcao_dada = input('Digite a função: ').strip().lower()
    if funcao_dada == 'fim':
        break
    ajuda(funcao_dada)