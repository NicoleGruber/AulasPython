#--- Exercicio 4  - Variávies e impressão com interpolacão de string
#--- Imprima a tela de um itinerário de viagem
#--- O itinerário deve conter o ponto de partida e de destino
#--- Entre os dois pontos deve conter no minimo 10 pontos de parada
#--- Cada item deve conter data, hora e descrição
#--- O itineário deve conter cabeçalho com o título da viagem
#--- Os dados de cada ponto devem estar em variáveis
#--- Deve ser usado os caracteres de tabulação, quebra de linha e a função Format()

titulo=('Viagem até Vancouver')
print('='*20,titulo,'='*20)

p=('Local de partida: Blumenau/SC/Brasil')
p1=('1ª Parada: Aeroporto de navegantes - Horario de chegada maxima até 9:00')
p2=('2ª Parada: Voo de Aeroporto de navegantes para Aeroporto Internacional de Sao Paulo - Embarque 10:00')
p3=('3ª Parada: Aeroporto Internacional de Sao Paulo - Chegada prevista 12:00')
p4=('4ª Parada: Voo de Aeroporto Internacional de Sao Paulo para Aeroporto Intercontinental George Bush - Embarque 16:00')
p5=('5ª Parada: Aeroporto Intercontinental George Bush - Chegada prevista 02:00')
p6=('6ª Parada: Voo de Aeroporto Intercontinental George Bush para Aeroporto internacional de Vancouver  - Embarque 08:00')
p7=('7ª Parada: Aeroporto internacional de Vancouver - Chegada prevista 13:00')
p8=('8ª Parada: Onibus até Ponte Suspensa de Capilano - Chegada prevista 14:00 - Horario de saida 16:30')
p9=('9ª Parada: Onibus até Stanley Park - Chegada prevista 17:00 - Horario de saida 19:00')
p10=('10ª Parada: Onibus até Blue Horizon Hotel - Chegada prevista 20:00 ')
d=('Local de destino: Vancouver/Colúmbia Britanica/Canadá')

print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(p,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,d))