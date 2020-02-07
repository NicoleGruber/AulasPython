# Aula 7  - 14-11-2019
# Dicionarios

# lista = []
# dicionario = {'nome':'Nicole', 'Sobrenome':'Gruber'}
# print(dicionario)
# print(dicionario['nome'])

# nome='Nicole'
# lista_notas = [10,10,9,10]
# media = sum(lista_notas)/len(lista_notas)
# situacao='reprovado'
# if media >=7:
#     situacao = 'aprovado'

# dicionario_alunos = {'nome':nome, 'lista_notas':lista_notas,'media':media,'situacao': situacao}

# print(f"{dicionario_alunos['nome']} - {dicionario_alunos['situacao']}")

# print(f"{dicionario_alunos['lista_notas']}")


dicionario_2 = {'Nome':''}
dicionario_2['Nome'] = 'Nicole'
dicionario_2['Nome'] = 'Gruber'

print(dicionario_2)

dicionario = {'nome':'Nicole', 'Sobrenome':'Gruber'}
dicionario ['Sobrenome'] = 'gru'
dicionario ['CPF'] = '001.117.979-26'

dicionario_pessoa={'Nome':'', 'Sobrenome':'', 'CPF':'','RG':''}
lista_pessoas = []
for i in range(1,11):
    dicionario_pessoa['Nome'] = input ('Digite seu nome: ')
    dicionario_pessoa['Sobrenome'] = input ('Digite seu Sobrenome: ')
    dicionario_pessoa['CPF'] = input ('Digite seu CPF: ')
    dicionario_pessoa['RG'] = input ('Digite seu RG: ')
    lista_pessoas.append(dicionario_pessoa)



