from functions.validação import lerInt
from functions.visual import titulo

titulo('Fatorial')
num = lerInt('Digite um número ínteiro: ')
fat = 1
if num < 0:
    print(f'{num}! = ', end='')
    for x in range(num, 0):
        fat *= x
        if x != -1:
            print(f'{x} x ', end='')
        else:
            print(f'{x} = {fat}')
elif num == 0:
    print('0! = 1')
else:
    print(f'{num}! = ', end='')
    for x in range(num, 0, -1):
        fat *= x
        if x != 1:
            print(f'{x} x ', end='')
        else:
            print(f'{x} = {fat}')
