from functions.validação import lerInt

dados = {}

while True:
    num = lerInt('Digite um número entre 1 e 999: ', pos=True, erro='Digite um valor válido')
    if 0 < num < 1000:
        break
    print('Um número entre 1 e 1000... Tente novamente')

if len(str(num)) == 1:
    dados['unidades'] = num
elif len(str(num)) == 2:
    dados['dezenas'] = num // 10
    dados['unidades'] = num - dados['dezenas'] * 10
else:
    dados['centenas'] = num // 100
    dados['dezenas'] = (num - dados['centenas'] * 100) // 10
    dados['unidades'] = (num - (dados['centenas'] * 100 + dados['dezenas'] * 10))

print(f'O número {num} possui ', end='')
for k, v in dados.items():
    if v != 0:
        if k != 'unidades':
            print(f'{v} {k}', end=', ')
        else:
            print(f'{v} {k}')
