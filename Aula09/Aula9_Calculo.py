from Aula09.Aula9_Calculos import soma, subtracao,divisao_fracionada,multiplicacao,divisao_inteira,raiz,resto_divisao

n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))


print(f'''A soma é {soma(n1, n2)} 
A subtração é {subtracao(n1,n2)}  
A multiplicação é {multiplicacao(n1,n2)}  
A divisão inteira é {divisao_inteira(n1,n2)} 
A divisão fracionada é {divisao_fracionada (n1,n2)} 
O resto da divisão é {resto_divisao(n1,n2)} 
A raiz é {raiz(n1,n2)}''')

