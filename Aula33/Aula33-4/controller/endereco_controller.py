from model.endereco import Endereco
from dao.endereco_db import Endereco_db

class EnderecoController:
    e = Endereco()
    e_db = Endereco_db()
    
    def listar_todos(self):
        return self.e_db.listar_todos()

    def exportar(self):
        lec = self.e_db.listar_todos()
        self.e.exportar_txt(lec)