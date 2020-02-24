# Aula 21 - 16-12-2019
#Funções para listas

from Aula27.exercicios.geradorlista import lista_simples_int


lista1 = lista_simples_int()
lista2 = lista_simples_int()
lista3 = lista_simples_int()


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print(len(lista1))

# 1.2) Qual é o maior valor da lista2?
print(max(lista2))

# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
maior = max(lista2)
menor = min(lista2)
print(maior + menor)

# 1.4) Qual é a média aritmética da lista1?
print(sum(lista1)/len(lista1))

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
soma1 = sum(lista1)
soma2 = sum(lista2)
soma3 = sum(lista3)
print(f'Lista 1 = {soma1} \nLista 2 = {soma2} \nLista 3 = {soma3} \nTotal = {soma1+soma2+soma3}')

# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
for valores in lista1:
    print(f'{valores}')

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
try:
    print(lista1[5], lista1[9], lista1[10], lista1[25])
except IndexError:
    print('A lista 1 não possui tantas posições.')

try:
    print(lista2[5], lista2[9], lista2[10], lista2[25])
except IndexError:
    print('A lista 2 não possui tantas posições.')

try:
    print(lista3[5], lista3[9], lista3[10], lista3[25])
except IndexError:
    print('A lista 3 não possui tantas posições.')
# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o
# tamanho delas).
if len(lista1) > len(lista2) and len(lista1) > len(lista3):
    print('A maior lista é a Lista 1.')
elif len(lista2) > len(lista1) and len(lista2) > len(lista3):
    print('A maior lista é a Lista 2.')
elif len(lista3) > len(lista1) and len(lista3) > len(lista2):
    print('A maior lista é a Lista 3.')
elif len(lista3) == len(lista1) and len(lista3) == len(lista2):
    print('As listas tem tamanhos iguais.')
elif len(lista1) == len(lista2) and len(lista1) > len(lista3):
    print('As listas 1 e 2 tem tamanhos iguais, e são maiores que a lista 3.')
elif len(lista1) == len(lista3) and len(lista1) > len(lista2):
    print('As listas 1 e 3 tem tamanhos iguais, e são maiores que a lista 2.')
elif len(lista2) == len(lista3) and len(lista2) > len(lista1):
    print('As listas 2 e 3 tem tamanhos iguais, e são maiores que a lista 1.')

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.
maior1 = max(lista1)
maior2 = max(lista2)
maior3 = max(lista3)
lista_menores = [min(lista1), min(lista2), min(lista3)]
menor = min(lista_menores)
print(f'Resultado: {(maior1+maior2+maior3)-menor}')

# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas
lista_maiores = [max(lista1), max(lista2), max(lista3)]
lista_menores = [min(lista1), min(lista2), min(lista3)]
maior = max(lista_maiores)
menor = min(lista_menores)
print(f'Resultado: {maior + menor}')
