#--- Aula 11 - 21-11-2019
#--- Prova

#--- 1- Crie um programa que calcule 
#---    imposto ISS de um serviço de desenvolvimento de software
#---    Utilizar metodos

#Exercicio 1
from Aula11.valores import iss
valor=float(input('Digite o valor do servico de desenvolvimento de software: '))
imposto=iss(valor)

print(f'O imposto sera {imposto}')


