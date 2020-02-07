# --- importando as classes
from Model.livro_model import LivroModel
from Dao.base_dao import BaseDao

# --- criando uma classe que tem como heranca a BaseDao(Chama o que tem na mae((BaseDao)
class LivroDao(BaseDao):

    # --- criando uma funcao para listar todos que tem no banco de dados
    def listar_todos(self):

        # --- retornando as informacoes dentro dos parametros que tem na LivroModel
        return self.sessao.query(LivroModel).all()