import sys
sys.path.append(r'C:\Users\Nicole\Desktop\AulasPython\Aula36')
from Aula36.Controller.pessoa_controller import PessoaController
from Aula36.Model.pessoa import Pessoa

pessoa = Pessoa()
pessoa.nome = 'Draeta1'
pessoa.sobrenome = 'Lindao'
pessoa.idade = 49
pessoa.endereco.logradouro = 'Rua dos Pombos1'
pessoa.endereco.numero = '0'
pessoa.endereco.complemento = 'casa muito engraçada'
pessoa.endereco.bairro = 'sem nome'
pessoa.endereco.cidade = 'gaspar'
pessoa.endereco.cep = '11111-000'

controller = PessoaController()
#id_salvo = controller.salvar(pessoa)
#pessoa_endereco = controller.buscar_por_id(id_salvo)
#print(pessoa_endereco)
print(controller.buscar_por_id(1))