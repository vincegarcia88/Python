import sqlite3
from time import sleep  

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

sleep(1)
print('--------Menu--------')
sleep(1)
print('1-Adicionar produto')
sleep(1)
print('2-Mostrar produtos')
sleep(1)
print('3-Alterar produto')

while True: 
    opcao = int(input('Digite uma das seguintes opções: '))
    
    if opcao == 1:
        adicionarProduto = input('Deseja adicionar novo produto? ')
        if adicionarProduto == 'sim':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            stock = int(input("Quantidade de stock: "))
            cursor.execute('''
                INSERT INTO produtos (nome, preco, stock)
                VALUES (?, ?, ?)
            ''', (nome, preco, stock))
            conn.commit()  # Salva as alterações no banco de dados
        else:
            continue  # Volta ao menu
    
    elif opcao == 2: 
        mostrarProdutos = input('Deseja ver todos os produtos? ')
        if mostrarProdutos == 'sim':
            cursor.execute('SELECT * FROM produtos')
            produtos = cursor.fetchall()
            for produto in produtos:
                print(produto)
        else: 
            continue  # Volta ao menu
    
    elif opcao == 3:
        alterarProduto = input('Deseja alterar algum produto? ')
        if alterarProduto == 'sim':
            escolha_id = int(input('Qual o id que deseja alterar? '))
            alteracao = input('Deseja alterar o nome, preco ou stock? ')

            if alteracao == 'nome':
                nome = input('Atualização nome: ')
                cursor.execute('''
                    UPDATE produtos SET nome = ?
                    WHERE id = ?
                ''', (nome, escolha_id))
            elif alteracao == 'preco':
                preco = float(input('Atualização preco: '))
                cursor.execute('''
                    UPDATE produtos SET preco = ?
                    WHERE id = ?
                ''', (preco, escolha_id))
            elif alteracao == 'stock':
                stock = int(input('Atualização stock: '))
                cursor.execute('''
                    UPDATE produtos SET stock = ?
                    WHERE id = ?
                ''', (stock, escolha_id))
            else:
                print('Opção inválida')
            conn.commit()  # Salva as alterações no banco de dados
        else:
            continue  # Volta ao menu
    
    else:
        print('Opção inválida, tente novamente')

conn.close()
