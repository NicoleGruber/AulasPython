class Endereco:
    id = 0
    rua = ''
    numero = ''
    complemento = ''
    bairro = ''
    cidade = ''
    cep = ''
    
    def exportar_txt(self,lista_enderecos):
        with open ('C:/Users/900156/Desktop/AulasPython/Aula33/Aula33-4/enderecos4.txt','a') as arquivo:
            for e in lista_enderecos:
                arquivo.write(f"{str(e)}\n")

    def __str__(self):
        return f"{self.id};{self.rua};{self.numero};{self.complemento};{self.bairro};{self.cidade};{self.cep}"