#--- Exercicio 5  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia o salário de uma pessoa
#--- Use o método 50-20-10-20 - https://www.jaseimevirar.com/blog/como-voce-organiza-seu-orcamento-mensal/
#--- Informe os percentuais e valores que a pessoa deve utilizar em cada categoria
#--- Deve ser utilizado a função format e os caracteres de tabulação e quebra de linha para cada categoria

salario = float(input('Digite o seu salario: '))
parte1 = salario*0.5
parte2 = salario*0.2
parte3 = salario*0.1
parte4 = salario*0.2
print('{} destinado a despesas fixas\n'.format(parte1))
print('{} destinado a investimentos de longo prazo como aposentadoria e independência financeir \n'.format(parte2))
print('{} destinado a investimentos de curto prazo, podendo ser uma reserva de emergência, uma viagem, um carro, etc;\n'.format(parte3))
print('{} para gastos livres e despesas variáveis\n'.format(parte4))