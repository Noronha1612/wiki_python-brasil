from functions.validação import lerInt

num = lerInt('Digite um número inteiro: ')

if num == 0:
    print('O valor 0 é nulo')
    exit()

primo = True
nprimos = []
if num < 0:
    for x in range(num + 1, -1):
        if num % x == 0:
            nprimos.append(x)
            primo = False
else:
    for x in range(num - 1, 1, -1):
        if num % x == 0:
            nprimos.append(x)
            primo = False

print('-='*35)
if primo:
    print(f'O valor {num} é primo')
else:
    print(f'O valor {num} NÃO é primo')
    print(f'Os valores que o dividiram (fora {num} e 1) foram: ', end='')
    for v in nprimos:
        print(v, end='; ')
    print()
print('-='*35)
