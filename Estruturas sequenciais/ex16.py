from functions.validação import lerFloat
from functions.visual import formatDinheiro
from math import ceil

area = lerFloat('Area em m²: ', pos=True, erro='Digite uma área válida.')
numlatas = ceil(area/54)
preço = formatDinheiro(numlatas * 80)

if area != 0:
    print(f'Para cobrir uma área de {area}m², você deverá comprar {numlatas} lata(s) de 18 litros')
    print(f'Valor total a se pagar: {preço}')
else:
    print(f'Não é necessário comprar alguma lata de tinta para pintar uma área de {area} m²')