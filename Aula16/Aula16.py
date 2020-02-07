# Aula 16 - 29-11-2019
#



# Cadastro de playlist
# Lendo musica, artista e album

from Aula16.faixa import criar_faixa,salvar_faixa,ler_faixa

musica=input('Digite uma musica: ')
album=input('Digite um album: ')
artista=input('Digite o artista: ')

faixa1 = criar_faixa(musica,album,artista)
salvar_faixa(faixa1)

lista = ler_faixa()
n=0
for faixa in lista:
    n+=1
    print(f"{n} - {faixa['musica']} - {faixa['album']} - {faixa['artista']}")

