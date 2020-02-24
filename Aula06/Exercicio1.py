#---- Exercício 1 - Listas
#---- Escreva um programa que leia o nome de 10 alunos
#---- Armazene os nomes em uma lista
#---- Imprima a lista

lista = []
for i in range(1,11):
    lista.append(input(f'Dgite o nome do aluno {i}: '))
print(lista)