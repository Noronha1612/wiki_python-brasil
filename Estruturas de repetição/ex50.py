from functions.validação import lerInt
from functions.visual import arredondamento

print('Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N')
n = lerInt('Digite a quantidade de termos de N para calcular o valor de H: ', pos=True, erro='Digite uma quantidade válida')

print('H = 1', end='')
den = h = 1
for x in range(n - 1):
    den += 1
    print(f' + 1/{den}', end='')
    h += 1 / den

print(f' = {arredondamento(h)}')
