from functions.validação import lerFloat, lerInt
from functions.visual import tabela

qtd = lerInt('Qauntos termos deseja digitar? ', pos=True, erro='Digite uma quantidade válida')
soma = maior = menor = 0

if qtd == 0:
    print('Até logo')
else:
    for x in range(qtd):
        while True:
            num = lerFloat(f'{x + 1}° Número: ')
            if 0 <= num <= 1000:
                break
            print('Digite um valor de 0 a 1000')
        if x == 0 or num > maior:
            maior = num
        if x == 0 or num < menor:
            menor = num
        soma += num
    
    dados = {
        'Quantidade de números': qtd,
        'Maior valor': maior,
        'Menor valor': menor,
        'Soma': soma
    }

    tabela(dados)
