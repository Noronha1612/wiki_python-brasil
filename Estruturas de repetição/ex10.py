from functions.validação import lerInt

inicio = lerInt('Início: ')
final = lerInt('Final: ')
if final == inicio:
    print('Paramêtros iguais...')
else:
    print('Contando...')
    if inicio < final:
        for v in range(inicio, final + 1):
            print(v, end=' ')
    else:
        for v in range(inicio, final - 1, -1):
            print(v, end=' ')
