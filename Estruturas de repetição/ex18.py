from functions.validação import lerInt, lerFloat
from functions.visual import tabela

qtd = lerInt('Quantos termos deseja digitar? ', pos=True, erro='Digite uma quantidade válida.')
soma = maior = menor = 0

if qtd == 0:
    print('Até a próxima!')
else:
    for x in range(qtd):
        num = lerFloat(f'{x + 1}° Número: ')
        if num > maior or x == 0:
            maior = num
        if num < menor or x == 0:
            menor = num
        soma += num
    dados = {
        'Quantidade de números': qtd,
        'Maior valor': maior,
        'Menor valor': menor,
        'Soma': soma
    }

    tabela(dados)

