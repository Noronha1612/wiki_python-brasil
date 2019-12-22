from functions.validação import lerInt
from functions.visual import titulo

titulo('Verificador de números primos')

num = lerInt('Digite um número inteiro: ', erro='NÚMERO INTEIRO...')

if num == 0:
    print('0 é um valor núlo')
    exit()

primo = True
if num > 0:
    for x in range(2, num):
        if num % x == 0:
            primo = False
else:
    for x in range(-2, num, -1):
        if num % x == 0:
            primo = False

if primo == False or num == 1 or num == -1:
    print(f'O valor {num} NÃO é primo')
else:
    print(f'O valor {num} é primo')