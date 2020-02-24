#--- Exercicio 1  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia dois números inteiros
#--- Realize as 4 operações matemáticas básicas com os números lidos
#--- Imprima os resultados das operações
#--- Informe qual número é maior ou se os dois são iguais

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
print(f'A soma do numero {n1} com o numero {n2} é = {soma}')
print(f'A subtração do numero {n1} com o numero {n2} é = {sub}')
print(f'A multiplicação do numero {n1} com o numero {n2} é = {multi}')
print(f'A divisão do numero {n1} com o numero {n2} é = {div}')

if n1 > n2:
    print(f'O numero {n1} é maior que o numero {n2}')
else:
    print(f'O numero {n2} é maior que o numero {n1}')