# --- importando o sqlalchemy e nomeando ele como db
import sqlalchemy as db

# --- criando a classe BaseDao
class BaseDao:

    # --- iniciando a classe BaseDao
    def __init__(self):

        # --- fazendo a conexao com o banco de dados
        self.conexao = db.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01")

        # --- criando uma variável que vai iniciar a sessao com o bancod de dados
        self.criador_sessao = db.orm.sessionmaker()

        # --- configurando a sessao para que conecte com o banco de dados
        self.criador_sessao.configure(bind = self.conexao)

        # --- criando uma variável que recebe a conexao
        self.sessao = self.criador_sessao()
