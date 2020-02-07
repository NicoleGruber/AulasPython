# --- importando a classe LivroDao
from Dao.Livro_dao import LivroDao

# --- salvando a classe em uma variável
dao = LivroDao()
# --- salvando o objeto da classe com o método listar todos em uma variável
livros = dao.listar_todos()
# --- um for para mostrar todos os dados
for l in livros:
    print(l)



















