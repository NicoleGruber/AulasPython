# --- importando o sqlalchemy e nomeando ele como db
import sqlalchemy as db

# --- importando o metodo que faz com que as informacoes venham como tabelas e salvando em uma variável
from sqlalchemy.ext.declarative import declarative_base
BaseAlchemy = declarative_base()

# --- criando a classe e passando como parametro o metodo
class LivroModel(BaseAlchemy):

    # --- definindo o nome da tabela que vai ser pego os dados
    __tablename__= "Nicole_Livros"

    # --- salvando em uma variável cada coluna da tabela e passando suas informacoes
    ID = db.Column(db.Integer,primary_key=True)
    NOME = db.Column(db.String(length=45))
    AUTOR = db.Column(db.String(length=45))
    ANO_PUBLICACAO = db.Column(db.String(length=45))

    # --- retornando os dados transformando-os em uma string
    def __str__(self):
        return f"ID : {self.ID} - Nome : {self.NOME} - Autor : {self.AUTOR} - Data Publicacao : {self.ANO_PUBLICACAO}"