from functions.validação import lerInt
from functions.visual import tabela

nums = []
for x in range(20):
    nums.append(lerInt(f'Digite o {x + 1}° número inteiro: ', erro='NÚMERO INTEIRO'))

pares = []
impares = []
for n in nums:
    if n % 2 == 0:
        if n not in pares:
            pares.append(n)
    else:
        if n not in impares:
            impares.append(n)

nums.sort()
pares.sort()
impares.sort()

tabela({
    'Números registrados': nums,
    'Números pares': pares,
    'Números ímpares': impares
}, tam=84)
