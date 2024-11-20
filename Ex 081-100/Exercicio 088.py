import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

cursor.execute ('''
    UPDATE produtos SET preco = 5.99
    WHERE id = 5
''')
cursor.execute ('''
    UPDATE produtos SET preco = 10.00
    WHERE id = 6
''')
cursor.execute ('''
    UPDATE produtos SET preco = 1.55
    WHERE id = 7
''')

conn.commit()
conn.close()