#===Classes===
#---Importando biblioteca do Mysql
import MySQLdb

#---Configurar a conexão
conexao = MySQLdb.connect(host = 'mysql.topskills.study', database = 'topskills01', user = 'topskills01', passwd = 'ts2019')

#---Salva o cursor da conexão em uma variável
cursor = conexao.cursor()

#---Criação do comando SQL e passado para o cursor 
comando_sql_select= "SELECT * FROM NicoleGruber"
cursor.execute(comando_sql_select)

#---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
resultado_select = cursor.fetchall()

#cria uma lista para armazenar os dicionarios
lista_pessoas = []
for p in resultado_select:
    dicionario_pessoa = {'ID' : 0 , 'Nome' : '' , 'Sobrenome' : '' , 'Idade' : 0 , 'Endereco_Id' : 0}
    dicionario_pessoa['ID'] = p[0]
    dicionario_pessoa['Nome'] = p[1]
    dicionario_pessoa['Sobrenome'] = p[2]
    dicionario_pessoa['Idade'] = p [3]
    dicionario_pessoa['Endereco_Id'] = p[4]
    lista_pessoas.append(dicionario_pessoa)

#---Abrindo arquivo, adicionando a lista de dicionario nele em formato pré-definido e fechando automaticamente
with open(r'C:\Users\Nicole\Desktop\AulasPython\Aula33\Aula33_1.txt','a')as arquivo:
    for p in lista_pessoas:
        arquivo.write(f"{p['ID']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_Id']}\n")