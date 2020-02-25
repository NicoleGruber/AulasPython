import sys
sys.path.append('C:/Users/900156/Desktop/AulasPython/Aula33/Aula33_4')
from Aula33.Aula33_4.controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)

from Aula33.Aula33_4.controller.endereco_controller import EnderecoController

ec = EnderecoController()
for e in ec.listar_todos():
    print(e)