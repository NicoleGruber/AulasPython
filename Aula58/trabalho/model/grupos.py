class GruposModel:
    def __init__(self,id,nome,descricao,data_criacao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.data_criacao = data_criacao

    def serialize(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "descricao" : self.descricao,
            "dataCriacao" : self.data_criacao
        }