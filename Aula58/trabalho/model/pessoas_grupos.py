class PessoaGrupoModel:
    def __init__(self,id,grupo_id,pessoa_id,data_entrada):
        self.id = id
        self.grupo_id = grupo_id
        self.pessoa_id = pessoa_id
        self.data_entrada = data_entrada

    def serialize(self):
        return {
            "id" : self.id,
            "grupoId" : self.grupo_id,
            "pessoaId" : self.pessoa_id,
            "dataEntrada" : self.data_entrada
        }