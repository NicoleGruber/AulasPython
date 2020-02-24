#---- Exercício 1 - Dicionario
#---- Escreva um programa que leia os dados de cerveja
#---- Cerveja: Marca, Tipo, IBU, ABV, EBC, Volume
#---- Crie um dicionario para armazenar os dados
#---- Imprima os dados do dicionário (não dicionário completo)

marca=input('Marca: ')
tipo=input('Tipo: ')
IBU=float(input('IBU: '))
ABV=float(input('ABV: '))
EBC=float(input('EBC: '))
volume=int(input('Volume: '))
 
dicionario = {'marca': marca, 'tipo': tipo, 'IBU': IBU, 'ABV': ABV,'EBC': EBC,'volume': volume}

print(f"marca: {dicionario['marca']}| tipo: {dicionario['tipo']} | IBU: {dicionario['IBU']} | ABV: {dicionario['ABV']} | EBC: {dicionario['EBC']} | Volume: {dicionario['volume']}")