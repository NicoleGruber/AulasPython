from flask import Flask
from pessoa_controller import Pessoa_Controller
from flask_restful import Api
app = Flask(__name__)
api = Api(app)
api.add_resource(Pessoa_Controller, '/api/Aula50')
@app.route('/')
def inicio():
    return 'Bem vindo a API'
app.run(debug=True, port=80)