from functions.visual import titulo
from functions.validação import lerInt

titulo('Tabuada')

while True:
    num = lerInt('Digite um número de 1 a 10: ')
    if 0 < num <= 10:
        break
    print('UM NÚMERO DE 1 A 10. Tente novamente...')

print('-='*12)
for x in range(10):
    print(f'{num} x {x + 1} = {(x+1)*num}')
print('-='*12)