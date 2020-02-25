from Aula33.Aula33_3.pessoa_db import listar_todos
from Aula33.Aula33_3.pessoa_converte import converter_tabela_dicionario
from Aula33.Aula33_3.pessoa_exporta import exportar_txt

lpt = listar_todos()
lpd = converter_tabela_dicionario(lpt)
exportar_txt(lpd)