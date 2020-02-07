# Aula 4 11-11-2019
# Estrutura de decisão

idade=int(input('Digite sua idade '))
#---- If simples, validação de apenas uma condição
if idade==18:
    print('Maior')
#---- If com else, 
#---- Caso a condição validada pelo If nao seja verdadeira,
#---- O Else é executado

if idade < 18:
    print('Menor')
else:
    print('Maior')

#---- If COM Elif e else
#---- Caso a condição validada no if seja falsa
#---- É validado a condição do Elif
#---- Caso a condição do Elif seja falsa
#---- Else é executado
if idade < 18:
    print ('De menor')
elif idade == 18:
    print('Fez agora')
else:
    print('Maior de idade')

#---- If com variável booleana
#---- Em caso de variável booleana, não é necessário a validação (==True)
#--- Pois o If ja valida o se o conteúdo da variável é True, senão vai para o Else
ativo = True
if ativo:
    print('Logar')
else:
    print('Não pode') 