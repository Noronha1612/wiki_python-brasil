from functions.validação import lerInt
from functions.visual import titulo

titulo('Fatorial')
while True:
    while True:
        num = lerInt('Deseja saber o fatorial de qual número? (máximo = 16 e mínimo = 0) ')
        if 0 <= num <= 16:
            break
        print('Digite uma opção válida.')

    if num == 0:
        print('0! = 1')
        exit()

    fat = 1
    print(f'{num}! = ', end='')
    for x in range(num, 0, -1):
        fat *= x
        if x != 1:
            print(x, end=' x ')
        else:
            print(f'{x} = {fat}')
    while True:
        esc = input('Deseja continuar? [S/N] ').lower().strip()[0]
        if esc in 'sn':
            break
        print('Selecione uma opção válida')
    if esc == 'n':
        break
    print('-='*35)
    
print('Até logo.')
    
