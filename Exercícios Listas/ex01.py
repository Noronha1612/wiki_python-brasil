from functions.validação import lerInt

numeros = []
for x in range(5):
    numeros.append(lerInt(f'Adicione o {x + 1}° número inteiro: '))

print('Os valores digitados foram: ', end='')
print(numeros)
