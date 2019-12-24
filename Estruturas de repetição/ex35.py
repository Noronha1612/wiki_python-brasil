from functions.validação import lerInt
from functions.visual import titulo


def verifPrimo(num):
    primo = True
    if num == 1 or num == -1:
        primo = False
    elif num > 0:
        for x in range(num - 1, 1, -1):
            if num % x == 0:
                primo = False
    else:
        for x in range(num + 1, -1):
            if num % x == 0:
                primo = False
    if primo:
        return True
    else:
        return False


titulo('Achador de números primos')

while True:
    num = lerInt('O programa vai achar todos os números primos entra 1 e N. Digite o valor de N: ')
    if num != 0:
        break
    print('O valor 0 é nulo... Tente outro')

if num > 0:
    print(f'Os valores primos entre 1 e {num} são: ', end='')
    for x in range(2, num):
        if verifPrimo(x):
            print(x, end=' ')
else:
    print(f'Os valores primos entre {num} e -1 são: ', end='')
    for x in range(-2, num, -1):
        if verifPrimo(x):
            print(x, end=' ')
print()
