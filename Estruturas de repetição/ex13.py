from functions.validação import lerFloat, lerInt
from functions.visual import titulo, arredondamento

titulo('Potência')

base = lerFloat('Base: ')
expoente = lerInt('Expoente: ')

res = base
if expoente == 0:
    res = 1
elif expoente > 0:
    for x in range(expoente - 1):
        res *= base
else:
    pot = base
    for x in range(expoente - 1):
        pot *= base
    res = 1/pot

arredondamento(res)
if expoente < 0:
    print('Resultado aproximado:', res)
else:
    print('Resultado:', res)