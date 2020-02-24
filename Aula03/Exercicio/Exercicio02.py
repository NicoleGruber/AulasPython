#--- Exercicio 2  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um cliente
#--- Cliente: Nome, Sobrenome, ano de nascimento
#--- Exiba uma mensagem de boas vindas para o cliente
#--- Exiba um menu: Produtos alcoolicos e Produtos não alcoolicos, Sair
#--- Caso o cliente seja menor de idade o item 'produtos alcoolicos' não deve ser exibido
#--- Leia a opção digitada e crie uma tela para cada opção

nome = input('Digite o nome do cliente: ')
sobrenome = input('Digite o sobrenome do cliente: ')
ano_nas = int(input('Digite o ano de nascimento: '))

print('Seja Bem Vindo!')
if ano_nas <= 2002:
    print('''========= Menu de Bebidas =========
1 - Bebidas Alcoolicas
2 - Bebidas não Alcoolicas
3 - Sair''')
    opcao = input('Digite a opcao desejada: ')
    if opcao == '1':
        print('''========= Bebidas Alcoolicas ========= 
        BUDWEISER
        CORONA
        STELLA ARTOIS
        SKOL BEATS SENSES''')
    elif opcao == '2':
        print('''========= Bebidas Alcoolicas ========= 
        H2OH!
        PEPSI
        GUARANÁ ANTARCTICA
        DO BEM LIMONADA''')
    elif opcao == '3':
        print('Finalizado com sucesso')
elif ano_nas >= 2003:
    print('''    
1 - Bebidas não Alcoolicas
2 - Sair
''')
    opcao = input('Digite a opcao desejada: ')
    if opcao == '1':
        print('''========= Bebidas Alcoolicas ========= 
        H2OH!
        PEPSI
        GUARANÁ ANTARCTICA
        DO BEM LIMONADA''')
    elif opcao == '2':
        print('Finalizado com sucesso')
