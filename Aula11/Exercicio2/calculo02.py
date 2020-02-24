def calculo_mes(valor,rent):
    valor_mes = valor*rent
    return valor_mes

def calculo_ano(valor,rent):
    montante=(valor*(1+rent)**12)-valor
    return montante
