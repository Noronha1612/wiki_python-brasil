from functions.validação import lerFloat

maior = 0
nummaior = []
for x in range(5):
    num = lerFloat(f'{x + 1}° Número: ')
    if maior == 0 or num >= maior:
        if num > maior:
            nummaior.clear()
        maior = num
        nummaior.append(x + 1)

print('-='*20)
if len(nummaior) == 1:
    print(f'O maior número registrado foi o {nummaior[0]}° número com o valor de {maior}.')
else:
    print('Os maiores números registrados foram o ', end='')
    for i, v in enumerate(nummaior):
        if i < len(nummaior) - 2:
            print(str(v) + '°', end=', ')
        elif i == len(nummaior) - 2:
            print(str(v) + '°', end=' e ')
        else:
            print(str(v) + '°', end=' ')
    print(f'número com o valor de {maior}')
print('-='*20)
