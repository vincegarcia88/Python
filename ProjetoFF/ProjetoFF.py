
import sqlite3
db = "projetofinal.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

def adicionar_tarefa(nome_da_tarefa, descricao_da_tarefa, id_status, id_prioridade):
    
    cursor.execute ("""INSERT INTO LISTA_DE_TAREFAS (NOME, DESCRICAO, ID_STATUS,ID_PRIORIDADE) 
                    VALUES (?,?,?,?)""", (nome_da_tarefa, descricao_da_tarefa, id_status, id_prioridade))
conn.commit()

def mostrar_tarefas(): #() Especifica as colunas onde os dados serão inseridos.
    cursor.execute("SELECT * FROM LISTA_DE_TAREFAS")
    rows = cursor.fetchall()

    if not rows:
        print("Não há tarefas pendentes.")

    else: 
        for row in rows:
            print(row)            
conn.commit()

def marcar_tarefa_concluida(id_tarefa):
    cursor.execute("UPDATE LISTA_DE_TAREFAS SET ID_STATUS = 2 WHERE ID_LISTA_DE_TAREFAS = ?", (id_tarefa,))
    rows = cursor.fetchall()

    if not rows:
        print("Não há tarefas a serem marcadas.")

    else: 
        for row in rows:
           print(row)

conn.commit()

    # SET ID_status = 2: Define o novo valor para a coluna ID_status. 
    # Aqui, você está assumindo que o valor 2 indica que a tarefa foi concluída.
    # WHERE ID_tarefas = ?: Especifica qual tarefa deve ser atualizada, 
    # usando um parâmetro para evitar injeção SQL.

def remover_tarefas_concluidas(id_tarefa):

    cursor.execute("DELETE FROM LISTA_DE_TAREFAS WHERE ID_LISTA_DE_TAREFAS = ?", (id_tarefa,))
    
    conn.commit()

def menu():    
    while True:
        print("\nMenu Principal")
        print("1. Adicionar Tarefa")
        print("2. Mostrar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefas Concluídas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_da_tarefa = input("Informe a tarefa: ")
            descricao_da_tarefa = input("Descreva a tarefa: ")
            id_prioridade = int(input("Indique a prioridade: \n[1] Baixa \n[2] Media \n[3] Alta: "))
            id_status = int(input("Indique o status da tarefa: \n[1] Concluido \n[2] Não Concluido: "))
        
            adicionar_tarefa(nome_da_tarefa, descricao_da_tarefa, id_prioridade, id_status)

        elif opcao == '2':
            mostrar_tarefas()            

        elif opcao == '3':
            id_tarefa = int(input("Informe o ID da tarefa a ser marcada como concluída: "))
            marcar_tarefa_concluida(id_tarefa)

        elif opcao == '4':
            print("\nEscolha o ID da tarefa a ser removida:")
            mostrar_tarefas()  # Mostra as tarefas antes de remover

            id_tarefa = int(input("\nInforme o ID da tarefa a ser removida: "))
            remover_tarefas_concluidas(id_tarefa)

        elif opcao == '5':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":

    menu()

