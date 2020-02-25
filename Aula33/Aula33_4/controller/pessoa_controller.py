from Aula33.Aula33_4.model.pessoa import Pessoa
from Aula33.Aula33_4.dao.pessoa_db import PessoaDb

class PessoaController:
    p = Pessoa()
    p_db = PessoaDb()

    def listar_todos(self):
        return self.p_db.listar_todos()

    def exportar(self):
        lpc = self.p_db.listar_todos()
        self.p.exportar_txt(lpc)
