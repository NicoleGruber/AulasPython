import sys
sys.path.append('C:/Users/900156/Desktop/AulasPython/Aula33/Aula33-4')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)