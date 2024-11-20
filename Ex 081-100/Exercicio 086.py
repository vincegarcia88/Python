import sqlite3

# Conectar ao banco de dados (ou criar um se não existir)
conn = sqlite3.connect('loja.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar a tabela 'produtos' com as colunas especificadas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        preco REAL,
        stock INTEGER
    )
''')

# Confirmar as mudanças no banco de dados
conn.commit()

# Fechar a conexão
conn.close()

print("Base de dados e tabela 'produtos' criadas com sucesso.")
