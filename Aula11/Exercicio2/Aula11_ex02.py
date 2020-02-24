#--- Aula 11 - 21-11-2019
#--- Prova
#--- 2-Crie um programa que calcule
#---    rentabilidade anual de um investimento
#---    baseando-se em sua rentabilidade mensal(juros compostos)
#---    a rentabilidade deve ser apresentada em % R$
#---    utilizar metodos
 
#Exercicio 2
from Aula11.Exercicio2.calculo02 import *

valor=float(input('Digite o valor investido: '))
rent=float(input('Digite a rentabilidade: '))

valor_mes=calculo_mes(valor,rent)
valor_ano=calculo_ano(valor,rent)

print(f'A rentabilidade aplicada foi de:{rent*100}% \n O lucro por mês sera de {valor_mes} \n O lucro por ano sera de: {valor_ano}')