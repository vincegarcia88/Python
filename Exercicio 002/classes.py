import sqlite3

class Biblioteca:
    """Classe responsável por gerenciar a biblioteca, incluindo operações no banco de dados."""
    def __init__(self, nome_db='biblioteca.db'):
        self.nome_db = nome_db  # Define o nome do banco de dados.

    def conectar(self):
        """Estabelece uma conexão com a base de dados."""
        return sqlite3.connect(self.nome_db)  # Retorna uma conexão com o banco de dados.

    def adicionar_livro(self, livro):
        """Adiciona um livro físico ou e-book ao banco de dados."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            
            # Verifica se o ISBN já existe na base de dados.
            cursor.execute("SELECT * FROM livros WHERE isbn = ?", (livro.isbn,))
            if cursor.fetchone():  # Se encontrar um registro, o livro já está cadastrado.
                print(f"Erro: O livro com ISBN {livro.isbn} já está cadastrado.")
                return
            
            # Comando SQL para inserir um novo livro na tabela.
            sql_inserir = '''
            INSERT INTO livros (titulo, autor, genero, isbn, tipo, stock, tamanho)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            # Define os valores a serem inseridos dependendo do tipo do livro.
            tipo = 'fisico' if isinstance(livro, LivroFisico) else 'ebook'
            stock = livro.stock if tipo == 'fisico' else None
            tamanho = livro.tamanho if tipo == 'ebook' else None
            cursor.execute(sql_inserir, (livro.titulo, livro.autor, livro.genero,
                                         livro.isbn, tipo, stock, tamanho))
            conn.commit()  # Confirma as alterações no banco de dados.
            print(f"Livro '{livro.titulo}' adicionado com sucesso.")

    def listar_livros(self):
        from utils import limpa
        """Lista todos os livros cadastrados no banco de dados."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM livros")  # Seleciona todos os registros da tabela 'livros'.
            livros = cursor.fetchall()  # Retorna todos os registros como uma lista de tuplas.
            
            for livro in livros:  # Itera sobre cada livro retornado.
                limpa()  # Limpa o terminal antes de exibir cada livro.
                id, titulo, autor, genero, isbn, tipo, stock, tamanho = livro
                # Formata a saída dependendo se é um livro físico ou e-book.
                if tipo == 'fisico':
                    print(f'ID: {id}\n--->ISBN: {isbn}\n--->Físico: {titulo}\n--->Autor: {autor}\n--->Gênero: {genero}\n--->Estoque: {stock}')
                    _ = input('Ver próximo...')  # Aguarda o usuário pressionar Enter.
                else:
                    print(f'ID: {id}\n--->ISBN: {isbn}\n--->Ebook: {titulo}\n--->Autor: {autor}\n--->Gênero: {genero}\n--->Tamanho: {tamanho}')
                    _ = input('Ver próximo...')  # Aguarda o usuário pressionar Enter.
            limpa()  # Limpa o terminal ao final da listagem.

    def devolver_livro(self, isbn):
        """Registra a devolução de um livro físico, aumentando o estoque."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            # Busca o livro físico pelo ISBN.
            sql_buscar = '''
            SELECT id, titulo, stock FROM livros WHERE isbn = ? AND tipo = 'fisico'
            '''
            cursor.execute(sql_buscar, (isbn,))
            livro = cursor.fetchone()
            
            if not livro:  # Verifica se o livro foi encontrado.
                print("Livro físico não encontrado para devolução.")
                return
            
            livro_id, titulo, stock = livro
            # Atualiza o estoque do livro devolvido.
            sql_devolver = '''
            UPDATE livros SET stock = stock + 1 WHERE id = ?
            '''
            cursor.execute(sql_devolver, (livro_id,))
            conn.commit()  # Confirma a devolução.
            print(f"Devolução registrada: {titulo}. Estoque atualizado: {stock + 1}")

    def vender_livro(self, isbn):
        """Registra a venda de um livro, reduzindo o estoque se for físico."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            # Busca o livro pelo ISBN.
            sql_buscar = '''
            SELECT id, titulo, stock, tipo FROM livros WHERE isbn = ?
            '''
            cursor.execute(sql_buscar, (isbn,))
            livro = cursor.fetchone()
            
            if not livro:  # Verifica se o livro foi encontrado.
                print("Livro não encontrado.")
                return
            
            livro_id, titulo, stock, tipo = livro
            
            if tipo == 'fisico':
                if stock > 0:  # Verifica se há estoque disponível.
                    # Reduz o estoque em 1.
                    sql_vender = '''
                    UPDATE livros SET stock = stock - 1 WHERE id = ?
                    '''
                    cursor.execute(sql_vender, (livro_id,))
                    conn.commit()  # Confirma a venda.
                    print(f"Venda registrada: {titulo}. Estoque atualizado: {stock - 1}")
                else:
                    print("Estoque insuficiente para venda.")
            else:
                print(f"Venda registrada: {titulo} (E-book).")  # E-books não têm estoque.

    def emprestar_livro(self, isbn):
        """Registra o empréstimo de um livro físico, reduzindo o estoque."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            # Busca o livro físico pelo ISBN.
            sql_buscar = '''
            SELECT id, titulo, stock FROM livros WHERE isbn = ? AND tipo = 'fisico'
            '''
            cursor.execute(sql_buscar, (isbn,))
            livro = cursor.fetchone()
            
            if not livro:  # Verifica se o livro foi encontrado.
                print("Livro físico não encontrado para empréstimo.")
                return
            
            livro_id, titulo, stock = livro
            
            if stock > 0:  # Verifica se há estoque disponível.
                # Reduz o estoque em 1.
                sql_emprestar = '''
                UPDATE livros SET stock = stock - 1 WHERE id = ?
                '''
                cursor.execute(sql_emprestar, (livro_id,))
                conn.commit()  # Confirma o empréstimo.
                print(f"Empréstimo registrado: {titulo}. Estoque atualizado: {stock - 1}")
            else:
                print("Estoque insuficiente para empréstimo.")  # Estoque insuficiente.

class Livro:
    """Classe base para representar um livro genérico."""
    def __init__(self, titulo, autor, genero, isbn):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn

    def __str__(self):
        return f"<Livro: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}>"

class LivroFisico(Livro):
    """Classe para representar livros físicos, herda de Livro."""
    def __init__(self, titulo, autor, genero, isbn, stock):
        super().__init__(titulo, autor, genero, isbn)  # Inicializa atributos da classe base.
        self.stock = stock  # Estoque disponível para o livro físico.

    def __str__(self):
        return f"<Livro Físico: {self.titulo}, Estoque: {self.stock}>"

class Ebook(Livro):
    """Classe para representar e-books, herda de Livro."""
    def __init__(self, titulo, autor, genero, isbn, tamanho):
        super().__init__(titulo, autor, genero, isbn)  # Inicializa atributos da classe base.
        self.tamanho = tamanho  # Tamanho do arquivo ou link de download do e-book.

    def __str__(self):
        return f"<Ebook: {self.titulo}, Tamanho: {self.tamanho}>"
