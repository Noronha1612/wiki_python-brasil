from functions.validação import lerInt
from functions.visual import tabela, titulo

titulo('Analisador de pares e ímpares')

pares = []
impares = []
for x in range(10):
    num = lerInt(f'Número {x + 1}: ')
    if num not in impares and num not in pares:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

pares.sort()
impares.sort()
txtpar = txtimpar = ''
for v in pares:
    txtpar += ' ' + str(v)
for v in impares:
    txtimpar += ' ' + str(v)
dados = {
    'Pares': txtpar,
    'Ímpares': txtimpar
} 

tabela(dados)
