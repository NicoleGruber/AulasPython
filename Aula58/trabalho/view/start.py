from flask import Flask
from flask_restful import Api

from Aula58.trabalho.Controller.grupoController import GrupoController
from Aula58.trabalho.Controller.pessoaGrupoController import PessoaGrupoController

app = Flask(__name__)
api = Api(app)

api.add_resource(GrupoController, '/api/grupo')
api.add_resource(PessoaGrupoController, '/api/pessoagrupo')

app.run(debug=True)