# 2 -
# Mercado Tech ----
# Solicitar nome do funcionario
# Solicitar idade
# Informar se o funcionario pode adquirir produtos alcoolicos

# 3 -
# Cadrastro Produtos Mercado Tech
# Solicitar o nome do produto
# Solicitar a categoria do produto (Alcoolicos e Não Alcoolicos)
# Exibir o produto cadastrado

nome = input('Digite o nome do funcionario: ')
sobrenome = input ('Digite o sobrenome do funcionario: ')
print(f'nome: {nome} sobrenome: {sobrenome}')
idade = int(input('Digite a idade do funcionario:'))

if idade>=18 :
    print('Você pode adquirir produtos alcoolicos')
    produto=input('Digite o nome do produto ')
    categoria =input('Produto alcoolico ou não alcoolico ')
    print(f'O seu Produto {produto} da categoria {categoria} foi cadastrado com sucesso')

else:
    print('Você não pode adquirir produtos alcoolicos')
    produto=input('Digite o nome do produto ')
    print(f'O seu produto {produto} de categoria não alcoolico foi cadastrado com sucesso')
