#--- Exercicio 4  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que realize a autenticação de usuário
#--- Crie duas variáveis para conter o usuário e senha padrão do sistema
#--- Leia o usuário e senha informados pelo usuário via função input()
#--- Valide se usuário e senha estão corretos
#--- Caso o usuário e senha estejam corretos informe com mensagem de boas vindas
#--- Caso o usuário e senha estejam incorretos informe com mensagem de falha de login

usuario_salvo = 'ABCDE'
senha_salvo = '12345'

usuario = input('Digite o usuario: ').strip()
senha = input('Digite a senha: ').strip()
if usuario == usuario_salvo:
    if senha == senha_salvo:
        print('''Seja Bem Vindo''')
    elif senha != senha_salvo:
        print('Falha de login, Senha incorreta')
elif usuario != usuario_salvo:
    print('Falha de login, Usuário incorreto')