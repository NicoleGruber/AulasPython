#---- Exercício 3 - Foreach
#---- Escreva programa que leia as notas (4) de 10 aluno
#---- Armazene as notas e os numes em listas
#---- Imprima:
#       1- O nome dos alunos
#       2- Média do aluno
#       3- Resultado (Aprovado>=7.0)

n1=0
n2=1
n3=2
n4=3

ListaAlunos = []
ListaNotas = []

for i in range(0,1) :
    ListaAlunos.append(input(f'Digite o nome do aluno {i+1}: '))
    for n in range(0,4):
        ListaNotas.append(float(input(f'Digite a nota {n+1}: ')))

for aluno in ListaAlunos:
    media=(ListaNotas[n1]+ListaNotas[n2]+ListaNotas[n3] + ListaNotas[n4])/4
    print(f'Aluno: {aluno} - resultado: ')
    print(f'Média: {media}')
    if media>= 7:
        print('Aprovado!')
    else:
        print('Reprovado!')

    n1 += 4
    n2 += 4
    n3 += 4
    n4 += 4             
