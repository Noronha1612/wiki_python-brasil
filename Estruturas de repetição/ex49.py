from functions.validação import lerInt
from functions.visual import arredondamento

n = lerInt('Quantos termos deseja mostrar? ', pos=True, erro='Digite uma quantidade válida')
if n == 0:
    print('Quantidade de termos nula')
    print('Programa encerrado...')
    exit()
if n == 1:
    print('Soma = 1/1 = 1')
    exit()

num = den = s = 1
print('Soma = 1/1 + ', end='')
for x in range(n - 1):
    num += 1
    den += 2
    s += num / den
    if x == n - 2:
        print(f'{num}/{den} = ', end='')
    else: 
        print(f'{num}/{den} + ', end='')
s = arredondamento(s)
print(s)
