from functions.validação import lerFloat

numeros = []
for v in range(3):
    numeros.append(lerFloat(f'{v + 1}° Número: '))
numeros.sort(reverse=True)

print('Os números digitados em ordem decrescente: ', end='')
for i, v in enumerate(numeros):
    if i != len(numeros) - 1:
        print(v, end='; ')
    else:
        print(v)
