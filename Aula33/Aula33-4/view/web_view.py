from flask import Flask, render_template
import sys
sys.path.append('C:/Users/900156/Desktop/AulasPython/Aula33/Aula33-4')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController

app = Flask(__name__)
pc = PessoaController()
ec = EnderecoController()
@app.route('/')
def inicio1():
    pessoas = pc.listar_todos()
    enderecos = ec.listar_todos()
    return render_template('index.html', lista1 = pessoas, lista2 = enderecos)

app.run()