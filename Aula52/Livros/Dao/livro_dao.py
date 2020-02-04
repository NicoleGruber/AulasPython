import MySQLdb

from Model.livro_model import LivroModel

class LivroDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()

    def listar_todos(self):
        self.cursor.execute(f"SELECT * FROM topskills01.Nicole_Livros;")
        livros = self.cursor.fetchall()
        lista_livros = []
        for l in livros:
            livro = LivroModel(l[1],l[2],l[3],l[0])
            lista_livros.append(livro.__dict__)
        return lista_livros

    def buscar_por_id(self,id):
        self.cursor.execute(f"SELECT * FROM topskills01.Nicole_Livros WHERE ID = {id}")
        livro = self.cursor.fetchone()
        l = LivroModel(livro[1],livro[2],livro[3],livro[0])
        return l.__dict__

    def adicionar(self,livro:LivroModel):
        self.cursor.execute(f"""INSERT INTO topskills01.Nicole_Livros 
        (NOME,AUTOR,ANO_PUBLICACAO)
        VALUES
        ('{livro.nome}','{livro.autor}','{livro.ano_publi}');""")
        self.connection.commit()
        id = self.cursor.lastrowid
        livro.id = id
        return livro.__dict__

    def alterar(self,livro:LivroModel):
        self.cursor.execute(f"""UPDATE topskills01.Nicole_Livros SET
        NOME = ('{livro.nome}'), 
        AUTOR = ('{livro.autor}'), 
        ANO_PUBLICACAO = ('{livro.ano_publi}')
        WHERE ID = ('{livro.id}')""")
        self.connection.commit()
        return livro.__dict__

    def remover(self,id):
        self.cursor.execute(f"DELETE FROM topskills01.Nicole_Livros WHERE ID = ('{id}')")
        self.connection.commit()
        return f'Removido Livro com o ID = {id}'
