from functions.validação import lerFloat
from functions.visual import formatDinheiro
from math import ceil, floor

area = lerFloat('Área em m²: ', erro='Digite uma área válida', pos=True)
print()
#Caso 1 - Apenas latas de 18 Litros
c1numlatas18 = ceil(area/108)
c1preco = formatDinheiro(c1numlatas18 * 80)

#Caso 2 - Apenas latas de 3,6 Litros
c2numlatas36 = ceil(area/21.6)
c2preco = formatDinheiro(c2numlatas36 * 25)

#Caso 3 - Mistura de latas de forma que o preço seja o menor
c3numlatas18 = floor(area / 108)
if area == c3numlatas18 * 108:
    c3numlatas36 = 0
else:
    arearestante = area - c3numlatas18 * 108
    litrosrestantes = arearestante / 6
    if litrosrestantes > 10.8:
        c3numlatas18 += 1
        c3numlatas36 = 0
    else:
        c3numlatas36 = ceil(litrosrestantes / 3.6)
c3preco = formatDinheiro(c3numlatas18 * 80 + c3numlatas36 * 25)

print(f"""Caso 1:
Número de latas de 18 litros: {c1numlatas18} lata(s)
Preço total: {c1preco} \n""")

print(f"""Caso 2:
Número de latas de 3,6 litros: {c2numlatas36} lata(s)
Preço total: {c2preco} \n""")

print(f"""Caso 3:
Número de latas de 18 litros: {c3numlatas18} lata(s)
Número de latas de 3,6 litros: {c3numlatas36} lata(s)
Preço total: {c3preco}""")