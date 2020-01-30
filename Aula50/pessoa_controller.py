from flask_restful import Resource

from dao.pessoa_dao import PessoaDao

class Pessoa_Controller(Resource):
    def __init__(self):
        self.dao = PessoaDao()

    def put(self):
        msg = self.dao.alterar(5)
        return msg

    def get(self):
        msg = self.dao.listar_todos()
        return msg

    def delete(self):
        msg = self.dao.remover(5)
        return msg

    def post(self):
        msg = self.dao.inserir()
        return  msg
