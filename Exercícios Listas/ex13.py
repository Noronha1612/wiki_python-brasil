from functions.validação import lerFloat, media
from functions.visual import arredondamento

meses = [ ['Janeiro'], 
    ['Fevereiro'],
    ['Março'],
    ['Abril'],
    ['Maio'],
    ['Junho'],
    ['Julho'],
    ['Agosto'],
    ['Setembro'],
    ['Outubro'],
    ['Novembro'],
    ['Dezembro']
]

temps = []

for ind, mes in enumerate(meses):
    temp = lerFloat(f'Digite a temperatura do mes de {mes[0]} em °C: ')

    temps.append(temp)
    meses[ind].append(temp)
    
tempMedia = media(temps)

mesesAcimaDaMedia = []

for mesEtemp in meses:
    if mesEtemp[1] > tempMedia:
        mesesAcimaDaMedia.append(mesEtemp)

print('-='*25)
print('Temperatura média anual: {}{}°C\33[m'.format("\33[1;34m" if tempMedia <= 25 else "\33[1;31m", arredondamento(tempMedia)))
print(f'\nMeses com temperaturas acima da media:')
for ind, mes in enumerate(mesesAcimaDaMedia):
    print(f'{ind + 1}- {mes[0]}({mes[1]}) ')
print('-='*25)
