# Crie um programa que leia 4 notas
# Imprima qual a maior
# Imprima a menor nota
# Imprima a media 
# Imprima se o aluno foi aprovado ou reprovado (media 7.0)
nota1=float(input('Primeira nota '))
nota2=float(input('Segunda nota '))
nota3=float(input('Terceira nota '))
nota4=float(input('Quarta nota '))
lista = [nota1, nota2 , nota3, nota4]
print('A maior nota foi:',max(lista))
lista = [nota1,nota2,nota3,nota4]
print('A menor nota foi:',min(lista))

if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:
    print(f'A nota {nota1} é a maior nota')
if nota2 > nota1 and nota2 > nota3 and nota2 > nota4:
    print(f'A nota {nota2} é a maior nota')
if nota3 > nota1 and nota3 > nota2 and nota3 > nota4:
    print(f'A nota {nota3} é a maior nota')
if nota4 > nota1 and nota4 > nota2 and nota4 > nota3:
    print(f'A nota {nota4} é a maior nota')
if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    print(f'A nota {nota1} é a menor nota')
if nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    print(f'A nota {nota2} é a menor nota')
if nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    print(f'A nota {nota3} é a menor nota')
if nota4 < nota1 and nota4 < nota2 and nota4 < nota3:
    print(f'A nota {nota4} é a menor nota')

media=int(4)
resultado= nota1 + nota2 + nota3 + nota4
resultado2= resultado/media
print (resultado2)
if resultado2 > 7.0:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado')

