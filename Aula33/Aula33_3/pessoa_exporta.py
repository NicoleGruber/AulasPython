def exportar_txt(lista_pessoas):
    #----- Cria um arquivo e atribui a uma variável 'arquivo'
    with open(r'C:\Users\Nicole\Desktop\AulasPython\Aula33\Aula33_3\Aula33-3.txt','a') as arquivo:
        #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
        for p in lista_pessoas:
            arquivo.write(f"{p['Id']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_Id']}\n")
