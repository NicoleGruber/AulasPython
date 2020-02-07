#--- Aula 11 - 21-11-2019
#--- Prova

#--- 1- Crie um programa para calcular o investimento
#---     
#---    Solicitar o valor a ser investido no Tesouro selic
#---    (Considerar o valor do tesouro selic hoje)
#---    Calcular o valor total ate o vencimento do titulo
#---    utilizar metodos
valor_investido=float(input('Quantas cotas do tesouro você quer comprar: '))

valor_inv=10410.00*valor_investido


taxa_selic=(5+0.02)/100

taxa_ate_vencimento=taxa_selic*5.33

valor_total=valor_inv + (valor_inv*taxa_ate_vencimento)

print (valor_total)

if valor_investido < 0.04:
    print('Essa compra não pode ser realizada, o valor minímo de compra é de 104.10')

