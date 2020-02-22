#--- Exercicio 3  - Variávies e impressão com interpolacão de string
#--- Imprima dois paragráfos do ultimo livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- Livro: Título, Edição, Autor, Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro


p1=(' Mas, enquanto gritava, outro jato de luz verde voou da varinha de Vol- \n demort contra Dumbledore e a serpente deu o bote...')
p2=(' Harry continuava parado com a mao na macaneta,mas nao tinha consci- \n encia disso. Olhava para Dumbledore quase sem respirar, prestando atencao, \n mas quase sem entender o que estava ouvindo. ')
titulo=('Harry Potter e a Ordem da Fenix')
edicao=('2')
autora=('J.K. Rowling')
data_publicacao=('11 de julho de 2007')
print(f'''Titulo: {titulo}
Edicão: {edicao}
Autora: {autora}
Data da Publicacão: {data_publicacao}
Paragrafo 1: {p1}
Paragrafo 2: {p2}''')