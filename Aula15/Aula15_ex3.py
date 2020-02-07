def salvar_dados(dados_cerveja):
    arquivo=open ('Aula15/aula15_ex3.txt','a')
    arquivo.write(f"{dados_cerveja['marca']};{dados_cerveja['tipo']};{dados_cerveja['teor']}\n")
    arquivo.close

def ler():
    lista=[]
    arquivo=open ('Aula15/aula15_ex3.txt','r')
    for linha in arquivo:
        linha=linha.strip()
        lista_cerveja=linha.split (';')
        cerveja={'marca':lista_cerveja[0],'teor':lista_cerveja[1],'tipo':lista_cerveja[2]}
        lista.append(cerveja)
    arquivo.close
    return lista

marca=input('Digite a marca da cerveja: ')
tipo=input('Digite o tipo da cerveja: ')
teor=float(input('Digite o teor da cerveja: '))

dados={'marca': marca ,'tipo': tipo, 'teor':teor}
salvar_dados(dados)

for cer in ler():
    print(f"marca:{cer['marca']} - teor:{cer['tipo']} - tipo:{cer['teor']}")


