from functions.validação import lerInt
from functions.visual import titulo

titulo('Fatorial')

num = lerInt('Deseja saber o fatorial de qual número? ')
print(f'Fatorial de {num}: ')
print(f'{num}!', end= ' = ')
fat = 1
if num == 0:
    print(fat)
elif num < 0:
    for x in range(num, 0):
        fat *= x
        if x != -1:
            print(x, end=' x ')
        else:
            print(x, end=' = ')
    print(fat)
else:
    for x in range(num, 0, -1):
        fat *= x
        if x != 1:
            print(x, end=' x ')
        else:
            print(x, end=' = ')
    print(fat)

