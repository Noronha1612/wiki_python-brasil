from functions.validação import lerFloat

numeros = []
for x in range(10):
    while True:
        n = lerFloat(f'Adicione o {x + 1}° número real: ')
        if n % 1 != 0:
            break
        print('VALOR REAL...')
    numeros.append(n)
numeros.sort(reverse=True)
print('Os valores digitados na ordem inversa é: ', end='')
print(numeros)
