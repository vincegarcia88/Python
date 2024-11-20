import sqlite3
import os



def limpa():
    """Função para limpar o terminal."""
    os.system("cls")  # No Windows, 'cls' limpa o terminal. Use 'clear' no Linux/Mac.

def criar_base_dados(nome_db='biblioteca.db'):
    """Função para criar a base de dados e a tabela 'livros'."""
    with sqlite3.connect(nome_db) as conn:  # Conecta ao banco de dados (cria se não existir).
        cursor = conn.cursor()  # Cria um cursor para executar comandos SQL.
        
        # Comando SQL para criar a tabela 'livros', se ela não existir.
        sql_criar_tabela = '''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,  
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            tipo TEXT CHECK(tipo IN ('fisico', 'ebook')) NOT NULL,
            stock INTEGER CHECK(stock >= 0),
            tamanho TEXT
        );
        '''
        cursor.execute(sql_criar_tabela)  # Executa o comando SQL para criar a tabela.
    print("Base de dados e tabela 'livros' configuradas com sucesso.")  # Mensagem de confirmação.

def menu():
    from classes import Biblioteca, Ebook, LivroFisico
    """Exibe o menu para o usuário interagir com a biblioteca."""
    biblioteca = Biblioteca()  # Instancia a classe Biblioteca.

    while True:
        limpa()  # Limpa o terminal.
        print("\nMenu Biblioteca:")
        print("1. Adicionar Livro")  # Opção para adicionar um livro.
        print("2. Listar Livros")  # Opção para listar todos os livros.
        print("3. Vender Livro")  # Opção para vender um livro.
        print("4. Emprestar Livro")  # Opção para emprestar um livro físico.
        print("5. Devolver Livro")  # Opção para devolver um livro físico.
        print("0. Sair")  # Sair do programa.
        
        opcao = input("Escolha uma opção: ")  # Solicita a opção do usuário.
        
        if opcao == "1":  # Adicionar livro.
            limpa()
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Gênero: ")
            isbn = input("ISBN: ")
            tipo = input("Tipo (fisico/ebook): ").lower()
            
            if tipo == 'fisico':  # Verifica se é um livro físico.
                stock = int(input("Estoque: "))
                livro = LivroFisico(titulo, autor, genero, isbn, stock)
            elif tipo == 'ebook':  # Verifica se é um e-book.
                tamanho = input("Tamanho do arquivo ou link: ")
                livro = Ebook(titulo, autor, genero, isbn, tamanho)
            else:
                print("Tipo inválido.")
                continue
            
            biblioteca.adicionar_livro(livro)

        elif opcao == "2":  # Listar livros.
            limpa()
            biblioteca.listar_livros()
        
        elif opcao == "3":  # Vender livro.
            limpa()
            isbn = input("Informe o ISBN do livro para venda: ")
            biblioteca.vender_livro(isbn)

        elif opcao == "4":  # Emprestar livro.
            limpa()
            isbn = input("Informe o ISBN do livro para empréstimo: ")
            biblioteca.emprestar_livro(isbn)

        elif opcao == "5":  # Devolver livro.
            limpa()
            isbn = input("Informe o ISBN do livro para devolução: ")
            biblioteca.devolver_livro(isbn)

        elif opcao == "0":  # Sair do programa.
            limpa()
            print("Saindo...")
            break

        else:  # Opção inválida.
            limpa()
            print("Opção inválida. Tente novamente.")
