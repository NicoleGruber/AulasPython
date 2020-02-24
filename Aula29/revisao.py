#----- Listas
coresL = ['Azul', 'Verde','azul-esverdeado']
#----- Tuplas
coresT = ('Azul', 'Verde','azul-esverdeado')
#----- Dicionários
coresD = {'Primária':'Azul', 'Secundária':'Verde', 'Terciárias':'azul-esverdeado'}

print(coresD)
print(coresT[1])
print(coresL[2])
print(coresD['Primária'])

for c in coresL:
    print(c)
