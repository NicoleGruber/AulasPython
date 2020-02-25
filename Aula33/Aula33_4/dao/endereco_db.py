import MySQLdb
from Aula33.Aula33_4.model.endereco import Endereco

class Endereco_db:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_select = 'SELECT * FROM NicoleGruber_Endereco'
        self.cursor.execute(comando_select)
        resultado = self.cursor.fetchall()
        lista_endereco_classe = self.converter_tabela_classe(resultado)
        return lista_endereco_classe

    def buscar_por_id(self,id):
        comando_select = f'SELECT * FROM NicoleGruber_Endereco WHERE ID = {id}'
        self.cursor.execute(comando_select)
        resultado = self.cursor.fechone()
        return resultado

    def converter_tabela_classe(self,lista_tuplas):
        lista_enderecos = []
        for e in lista_tuplas:
            e1 = Endereco() 
            e1.id = e[0]
            e1.rua = e[1]
            e1.numero = e[2]
            e1.complemento = e[3]
            e1.bairro = e[4]
            e1.cidade = e[5]
            e1.cep = e[6]
            lista_enderecos.append(e1)
        return lista_enderecos
