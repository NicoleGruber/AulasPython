from flask_restful import Resource
from flask import request

from Model.livro_model import LivroModel
from Dao.livro_dao import LivroDao

class LivroController(Resource):
    def __init__(self):
        self.dao = LivroDao()

    def get (self,id = None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar_todos()

    def post(self):
        nome = request.json['nome']
        autor = request.json['autor']
        ano_publi = request.json['ano_publi']
        livro = LivroModel(nome, autor, ano_publi)
        return self.dao.adicionar(livro)

    def put(self,id):
        nome = request.json['nome']
        autor = request.json['autor']
        ano_publi = request.json['ano_publi']
        livro = LivroModel(nome, autor, ano_publi,id)
        return self.dao.alterar(livro)

    def delete(self,id):
        return self.dao.remover(id)
