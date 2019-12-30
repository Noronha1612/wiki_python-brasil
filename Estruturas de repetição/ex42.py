from functions.validação import lerInt
from functions.visual import tabela
from time import sleep

c1 = c2 = c3 = c4 = 0
while True:
    num = lerInt('Digite um número inteiro (digite um número negativo para parar) : ')
    if num < 0:
        break
    if num > 100:
        print('Digite um número menor que 100')
        continue
    if num < 26:
        c1 += 1
    elif num < 51:
        c2 += 1
    elif num < 76:
        c3 += 1
    else:
        c4 += 1
    print('Dado salvo com sucesso')

dados = {
    'Foram contados os valores no seguinte intervalo':'',
    '0 - 25': c1,
    '26 - 50': c2,
    '51 - 75': c3,
    '76 - 100': c4
}
print('Contando...')
sleep(1.7)
tabela(dados)
