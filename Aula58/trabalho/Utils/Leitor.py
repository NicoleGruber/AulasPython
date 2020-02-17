
class Leitor:
    def __init__(self, nomeArquivo, classe):
        self.nomeArquivo = nomeArquivo
        self.model = classe

    def ler(self):
        with open(self.nomeArquivo, 'r') as arquivo:
            ret = []
            for i in arquivo:
                a = i.strip().split(";")
                m = self.model(*a)
                ret.append(m.serialize())

        return ret