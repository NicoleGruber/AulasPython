#===referencia ao Mysql===

import MySQLdb
#---listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM NicoleGruber')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)
        
#---buscar uma pessoa pelo ID
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM NicoleGruber WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#---buscar pessoas por sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM NicoleGruber WHERE SOBRENOME like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)

#---salvar pessoa
def salvar(cn, cr, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"INSERT INTO NicoleGruber (NOME, SOBRENOME, IDADE, ENDERECO_ID )VALUES('{nome}', '{sobrenome}',{idade},{endereco_id})")
    cn.commit()

#---alterar pessoa
def alterar(cn, cr, id, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"UPDATE NicoleGruber SET NOME='{nome}', SOBRENOME='{sobrenome}', IDADE={idade}, ENDERECO_ID={endereco_id} WHERE ID={id} ")
    cn.commit()

#---deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM NicoleGruber WHERE ID={id}')
    cn.commit()

conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019' )
cursor = conexao.cursor()

#---Chamando os metodos
# listar_todos(cursor)
# buscar_por_id(cursor, 3)
# buscar_por_sobrenome(cursor,'Gru')
# salvar(conexao, cursor, 'Lua', 'Gruber', 4,1)
# alterar(conexao, cursor, 8, 'Gugu Voltolini', 'KingOfBasquete', 17, 5)
# deletar(conexao, cursor, 7)

#---listar todos os endereços 
def listar_todos(d):
    d.execute('SELECT * FROM NicoleGruber_Endereco')
    enderecos = d.fetchall()
    for e  in  enderecos:
        print(e)
        
#---buscar um endereco pelo ID
def buscar_por_id(d, id):
    d.execute(f'SELECT * FROM NicoleGruber_Endereco WHERE ID = {id}')
    enderecos = d.fetchone()
    print(enderecos)

#---buscar enderecos por rua
def buscar_por_rua(d, rua):
    d.execute(f"SELECT * FROM NicoleGruber_Endereco WHERE RUA like '{rua}%' ")
    for e  in  d.fetchall():
        print(e)
#---buscar enderecos por cidade
def buscar_por_cidade(d,cidade):
    d.execute(f"SELECT * FROM NicoleGruber_Endereco WHERE CIDADE like '{cidade}%' ")
    for e in d.fetchall():
        print(e) 
#---buscar endereco por bairro
def buscar_por_bairro(d,bairro):
    d.execute(f"SELECT * FROM NicoleGruber_Endereco WHERE BAIRRO like '{bairro}%' ")
    for e in d.fetchall():
        print(e)
#---salvar endereco
def salvar(cn, cr, rua, numero ,bairro, cidade, cep, complemento='NULL'):
    cr.execute(f"INSERT INTO NicoleGruber_Endereco (RUA, NUMERO, COMPLEMENTO, BAIRRO, CIDADE, CEP )VALUES('{rua}',{numero},'{complemento}','{bairro}','{cidade}','{cep}')")
    cn.commit()

#---alterar endereco
def alterar(cn, cr,id, rua, numero , bairro, cidade, cep, complemento= 'NULL'):
    cr.execute(f"UPDATE NicoleGruber_Endereco SET RUA='{rua}', NUMERO={numero}, COMPLEMENTO='{complemento}', BAIRRO='{bairro}',CIDADE='{cidade}',CEP='{cep}' WHERE ID={id}")
    cn.commit()

#---deletar endereco por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM NicoleGruber_Endereco WHERE ID={id}')
    cn.commit()
    
#---Chamando os metodos
# listar_todos(cursor)
# buscar_por_id(cursor,2)
# buscar_por_rua(cursor,'m')
# buscar_por_cidade(cursor,'BLUMENAU')
# buscar_por_bairro(cursor,'salto')
# salvar(conexao,cursor,'ABC',74,'GARCIA','BLUMENAU','33353-222','APTO 206')
# alterar(conexao,cursor,8,'xxx','74','bbb','ddddd','3-222','APTO 203')
# deletar(conexao,cursor,8)

