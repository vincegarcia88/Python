"""def limpa ():

import os

os.system("cls")

print("Olá mundo!")
_ = input("Clique para continuar")

limpa()

print("Apagou tudo")"""

#CRIAR BASE DE DADOS E TABELA

"""with sqlite3.connect("base_teste.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS alunos(
                   id INTEGER PRIMARY KEY,
                   nome TEXT,
                   contacto INTEGER
                   )""")
    conn.commit()

    print(f"Dados inseridos com sucesso!")"""

"""#INSERIR DADOS NA TABELA DA BASE DE DADOS
nome = input("Digite o seu nome: ")
contacto = input("Digite o seu contacto: ")

with sqlite3.connect (db) as conn:
    cursor = conn.cursor()

    cursor.execute("INSERT INTO alunos (nome, contacto)
                   VALUES (?, ?)",(nome, contacto) )
    
    conn.commit()
    print("Dados inseridos com sucesso")

#LER LINHAS DA TABELA DA BASE DE DADOS
with sqlite3.connect(db) as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")
    dado = cursor.fetchone()

    print(f"ID: {dado[0]}\nNOME: {DADO[1]}\nCONTACTO {dado[2]}")
    



