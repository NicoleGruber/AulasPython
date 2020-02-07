#---- Exercício 2 - For
#---- Escreva programa que leia um numero inteiro
#---- Calcule a taboada do numero informado
#---- Imprima a taboada com a conta completa (n * i = r)
n1=int(input('Digite um numero: '))
for i in range (0,11):
    print(f'{i} x {n1} = {i*n1}')