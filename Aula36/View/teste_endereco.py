import sys
sys.path.append(r'C:\Users\Nicole\Desktop\AulasPython\Aula36')
from Aula36.Controller.endereco_controller import EnderecoController
from Aula36.Model.endereco import Endereco

end = Endereco()
end.logradouro = 'Rua dos Pombos123'
end.numero = '0'
end.complemento = 'casa muito engraçada'
end.bairro = 'sem nome'
end.cidade = 'gaspar'
end.cep = '11111-000'
end.id = 123

contr=  EnderecoController()
id_salvo = contr.salvar(end)
print(contr.buscar_por_id(id_salvo))