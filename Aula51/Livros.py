from flask import Flask
from flask_restful import Api

from Aula51.Controller.livros_controller import LivroController

app = Flask(__name__)
api = Api(app)

api.add_resource(LivroController, '/api/livro', endpoint = 'livros')
api.add_resource(LivroController, '/api/livro/<int:id>', endpoint = 'livro')

app.run(debug=True)