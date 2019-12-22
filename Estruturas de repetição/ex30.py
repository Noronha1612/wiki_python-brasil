from functions.visual import formatDinheiro, titulo

titulo('Panificadora Pão de Ontem')

for x in range(50):
    print(f'{x + 1:.<20}{formatDinheiro((x + 1) * 0.18)}')
