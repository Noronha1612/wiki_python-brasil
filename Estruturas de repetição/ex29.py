from functions.visual import formatDinheiro, titulo

titulo('Lojas Quase Dois')

for x in range(50):
    print(f'{x + 1:.<20}{formatDinheiro((x + 1) * 1.99)}')
