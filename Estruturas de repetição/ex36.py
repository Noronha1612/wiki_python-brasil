from functions.validação import lerInt, lerFloat
from functions.visual import titulo, arredondamento

titulo('Tabuada limitada')

num = lerFloat('Deseja mostrar a tabuada de qual número? ')
if num == 0:
    print('Todos números na tabuada de 0 resultam em 0')
    exit()

com = lerInt('Começo: ')

while True:
    fin = lerInt('Final: ')
    if fin >= com:
        break
    print('O final não pode ser menor que o começo por questões óbvias...')

print('-='*15)
print('Tabuada:')
for x in range(com, fin + 1):
    print(f'{num} x {x} = {arredondamento(num * x)}')
print('-='*15)
