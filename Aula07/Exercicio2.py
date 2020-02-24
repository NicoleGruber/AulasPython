#---- Exercício 2 - Dicionario
#---- Escreva um programa que leia os dados de 11 jogadores
#---- jogador: Nome, Posicao, Numero, PernaBoa 
#---- Crie um dicionario para armazenar os dados
#---- Imprima todos os jogadores e seus dados


lista_jogadores= []

for i in range (1,12):
    Nome=input('Digite  o nome do jogador: ')
    Posiçao=input('Digite a posiçao do jogador: ')
    Numero=int(input('Digite o numero do jogador: '))
    PernaBoa=input('Digite a Perna Boa do jogador: ')

    dicionario = {'Nome': Nome, 'Posiçao': Posiçao, 'Numero': Numero, 'PernaBoa': PernaBoa}

    lista_jogadores.append(dicionario)
    
for dicionario in lista_jogadores:
    print(f"Nome= {dicionario['Nome']}, Posiçao= {dicionario['Posiçao']}, Numero= {dicionario['Numero']}, PernaBoa= {dicionario['PernaBoa']}")
    