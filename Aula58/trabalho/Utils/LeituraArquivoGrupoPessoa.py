from Aula58.trabalho.model.pessoas_grupos import PessoaGrupoModel

class LeituraGrupoPessoa:
    def leitura(self):
        with open(r"C:\Users\900156\Desktop\Trabalho\GrupoPessoa.txt", 'r') as arquivo:
            lista_grupos = []
            for linha in arquivo:
                lista_linha = linha.strip().split(';')
                pg = PessoaGrupoModel(*lista_linha)
                lista_grupos.append(pg.serialize())

        return lista_grupos