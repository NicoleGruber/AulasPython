#--- Exercicio 5  - Variávies e impressão com interpolacão de string
#--- Imprima os dados de 5 papeis cotatos na bolsa de valors de SP
#--- Os dados dos papeis devem estar em variáveis
#--- Papel: Nome, Tipo, Cotação Atual e Valores Min e Max do dia
#--- A tela deve conter cabeçalho e rodapé

nome1 = 'PETROBRAS ON'
tipo1 = 'Ordinário'
cot1 = 29,30
valmin1 = 31,59
valmax1 = 32,51

nome2 = 'BRADESCO PN'
tipo2 = 'Preferencial'
cot2 = 33,35
valmin2 = 33,16
valmax2 = 33,63

nome3 = 'ITAUUNIBANCO PN'
tipo3 = 'Preferencial'
cot3 = 35,68
valmin3 = 35,79
valmax3 = 35,16

nome4 = ' GERDAU PN'
tipo4 = 'Preferencial'
cot4 = 15,55
valmin4 = 15,7
valmax4 = 15,53

nome5 = ' OI PN'
tipo5 = 'Ordinário'
cot5 = 1,00
valmin5 = 0,98
valmax5 = 1,2

p1=(f' Nome: {nome1} \n Tipo: {tipo1} \n Cotacão Atual: {cot1} \n Valores min e max do dia: {valmin1} - {valmax1}')
p2=(f' Nome: {nome2} \n Tipo: {tipo2} \n Cotacão Atual: {cot2} \n Valores min e max do dia: {valmin2} - {valmax2}')
p3=(f' Nome: {nome3} \n Tipo: {tipo3} \n Cotacão Atual: {cot3} \n Valores min e max do dia: {valmin3} - {valmax3}')
p4=(f' Nome: {nome4} \n Tipo: {tipo4} \n Cotacão Atual: {cot4} \n Valores min e max do dia: {valmin4} - {valmax4}')
p5=(f' Nome: {nome5} \n Tipo: {tipo5} \n Cotacão Atual: {cot5 }\n Valores min e max do dia: {valmin5} - {valmax5}')

print('============== BOLSA DE VALORES ==============')
print(f'{p1}\n\n{p2}\n\n{p3}\n\n{p4}\n\n{p5}')
print('==============================================')