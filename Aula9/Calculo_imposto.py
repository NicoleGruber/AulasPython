from Aula9.impostos import calculo_inss, calculo_irrf

print('='*50 ,'\n')

nome=input('Digite seu nome: ')
cpf=input('Digite seu CPF: ')
num_registro=int(input('Digite seu numero de registro: '))
cargo=input('Digite seu cargo: ')
salario=float(input('Digite seu salario: '))

inss=calculo_inss(salario)
irrf=calculo_irrf(salario,inss)

salario_liquido= salario-inss-irrf

print(f'Inss: {inss}')
print(f'Irrf: {irrf}')
print(f'Seu salario liquido é {salario_liquido}')

print('\n','='*50)


