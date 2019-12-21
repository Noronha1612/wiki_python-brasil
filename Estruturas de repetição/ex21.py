from functions.validação import lerInt

num = lerInt('Digite um número inteiro: ')

if num == 0:
    print('O valor 0 é nulo')
    exit()

primo = True
if num < 0:
    for x in range(num + 1, -1):
        if num % x == 0:
            primo = False
else:
    for x in range(num - 1, 1, -1):
        if num % x == 0:
            primo = False

if primo:
    print(f'O valor {num} é primo')
else:
    print(f'O valor {num} NÃO é primo')
