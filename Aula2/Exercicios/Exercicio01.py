#--- Exercicio 1  - Variávies e impressão com interpolacão de string
#--- Crie 5 variávies para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Os dados devem ser impressos utilizando a funcao format()
#--- Deve ser usado apenas uma vez a função print(), porem os dados devem ser apresentados um em cada linha
#--- O salario deve ser de tipo flutuante e na impressão deve apesentar apenas duas casas após a vírgula

nome = input('Digite o nome do Funcionario: ')
sobrenome = input('Digite o sobrenome do Funcionario: ')
cpf = input('Digite o cpf do Funcionario: ')
rg = input('Digite o rg do Funcionario: ')
salario = float(input('Digite o salario do Funcionario: '))

print('''Nome: {} 
Sobrenome: {}
CPF: {}
RG: {}
Salario: {:.2f}'''.format(nome,sobrenome,cpf,rg,salario))