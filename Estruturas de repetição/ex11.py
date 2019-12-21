from functions.validação import lerInt

soma = 0
inicio = lerInt('Início: ')
final = lerInt('Final: ')
if final == inicio:
    print('Paramêtros iguais...')
else:
    print('Contando...')
    if inicio < final:
        for v in range(inicio, final + 1):
            soma += v
            print(v, end=' ')
    else:
        for v in range(inicio, final - 1, -1):
            soma += v
            print(v, end=' ')
if final != inicio:
    print()
    print(f'Soma: {soma}')