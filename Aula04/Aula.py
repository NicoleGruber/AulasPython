#Aula 4
#Fazer um programa que leia 2 numeros   
#Realize as 4 operacoes matematicas
#Imprima o resultado das operações
#Diga qual numero é o maior

n1=int(input('Primeiro numero'))
n2=int(input('Segundo numero'))

resultado=n1+n2
print(resultado)
resultado=n1-n2
print(resultado)
resultado=n1*n2
print(resultado)
resultado=n1/n2
print(resultado)

if(n1)==(n2):
   print (f'O numero {n1} é igual ao numero {n2}')
elif(n1)>(n2):
   print (f'O numero {n1} é maior que o numero {n2}')
else:
   print (f'O numero {n1} é menor que o numero {n2}')

