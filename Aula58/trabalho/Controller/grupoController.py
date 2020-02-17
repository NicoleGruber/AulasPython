from flask_restful import Resource

from Aula58.trabalho.Utils.Leitor import Leitor
from Aula58.trabalho.model.grupos import GruposModel

class GrupoController(Resource):
    def __init__(self):
        self.ag = Leitor(r'C:\Users\900156\Desktop\AulasPython\Aula58\trabalho\grupos.txt', GruposModel)

    def get(self):
        return self.ag.ler()

    def post(self):
        return None

    def delete(self):
        return None

    def put(self):
        return None