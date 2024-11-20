import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

# Lista para armazenar os produtos
produtos = []

# Solicitar ao usuário os detalhes de 10 produtos
for i in range(10):
    print(f"Insira os detalhes do produto {i + 1}:")

    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    stock = int(input("Quantidade de stock: "))
    
    # Adicionar os detalhes do produto como uma tupla na lista
    produtos.append((nome, preco, stock))

# Usar executemany() para inserir vários registros de uma só vez
cursor.executemany('''
    INSERT INTO produtos (nome, preco, stock)
    VALUES (?, ?, ?)
''', produtos)

# Confirmar as alterações no banco de dados
conn.commit()

# Fechar a conexão
conn.close()

print("Os produtos foram inseridos com sucesso!")



