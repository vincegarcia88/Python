# TABELAS SQL

import sqlite3
db = "projetofinal.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute ("""CREATE TABLE IF NOT EXISTS STATUS(
                ID_STATUS INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME_status VARCHAR
                )""")

cursor.execute ("""CREATE TABLE IF NOT EXISTS PRIORIDADE(
                ID_PRIORIDADE INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME VARCHAR
                )""")

cursor.execute ("""CREATE TABLE IF NOT EXISTS LISTA_DE_TAREFAS(
                ID_LISTA_DE_TAREFAS INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME VARCHAR,
                DESCRICAO VARCHAR,
                ID_STATUS INTEGER,
                ID_PRIORIDADE VARCHAR,
                FOREIGN KEY (ID_PRIORIDADE) REFERENCES prioridade (ID_PRIORIDADE),
                FOREIGN KEY (ID_STATUS) REFERENCES status(ID_STATUS))""")

conn.commit()
