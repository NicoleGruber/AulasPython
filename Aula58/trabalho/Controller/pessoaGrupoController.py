from flask_restful import Resource

from Aula58.trabalho.Utils.Leitor import Leitor
from Aula58.trabalho.model.pessoas_grupos import PessoaGrupoModel

class PessoaGrupoController(Resource):
    def __init__(self):
        self.l = Leitor(r"C:\Users\900156\Desktop\AulasPython\Aula58\trabalho\GrupoPessoa.txt", PessoaGrupoModel)

    def get(self):
        return self.l.ler()
    

    def post(self):
        return None

    def delete(self):
        return None

    def put(self):
        return None