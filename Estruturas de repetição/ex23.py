from functions.validação import lerInt
from functions.visual import titulo

titulo('Analisador de números primos')
print('O programa irá analisar todos os números de 1 até N* e irá dizer quais desses números são primos.')
print('* N é um input digitado pelo usuário.')
n = lerInt('Digite um número inteiro para o valor de N: ')

nprimos = []
c = 0
if n > 0:
    for x in range(2, n + 1):
        primo = True
        for y in range(x - 1, 1, -1):
            c += 1
            if x % y == 0:
                primo = False
        if primo:
            nprimos.append(x)

else:
    for x in range(n, -1):
        primo = True
        for y in range(x + 1, -1):
            c += 1
            if x % y == 0:
                primo = False
        if primo:
            nprimos.append(x)
    nprimos.sort(reverse=True)

if len(nprimos) == 0:
    print('~'*40)
    print('Não há valores primos nesse intervalo')
    print('~'*40)
    exit()
print('~'*80)
print(f'Quantidade de testes realizados: {c} vezes')
print(f'Números primos no intervalo de 1 até {n}: ')
for i, v in enumerate(nprimos):
    if i != len(nprimos) - 1:
        print(v, end='; ')
    else:
        print(v)
print('Até logo'.center(80, '~'))