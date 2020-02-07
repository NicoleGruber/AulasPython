# Lista
lista1 = []

# ---Inicialização de uma variável lista,com elementos
lista2 = ['Marcela', 'Nicole', 'Matheus',10]

#----Lista de inteiros
lista3 = [1,2,3,4,5]

#----lista de tipos diferentes
lista4 = [1,'Nicole',12.5]

#----Impressão das listas criadas
print(lista1)
print(lista2)
print(lista3)
print(lista4)

#---- Adicionando elementos em uma lista ja criada
lista1.append(lista2)
lista1.append(lista3)

#---- Impressao das listas modificadas
print(lista1)
print(lista2)
print(lista3)

#---- Criacao de lista com dados vindos da função Input
lista_perguntas = [input('Digite seu artista favorito'), input('Digite seu guitarrista favorito')] 
print(lista_perguntas)

#---- Recuperando um dado de uma posição específica da lista
posicao = int(input('Digite a posicao: '))
print( lista2[posicao-1] )


