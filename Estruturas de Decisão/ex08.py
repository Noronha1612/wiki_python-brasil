from functions.validação import lerFloat
from functions.visual import formatDinheiro

preços = []
for v in range(3):
    preços.append(lerFloat(f'Preço do Produto {v + 1}: R$', pos=True, erro='Digite uma quantia válida.'))
menorpreço = f'Produto {preços.index(min(preços)) + 1}'

print(f'O produto que você deve comprar é o {menorpreço}')
print(f'Pois possui o valor de {formatDinheiro(min(preços))}')