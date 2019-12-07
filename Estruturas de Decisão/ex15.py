from functions.validação import lerFloat

print('-=-=-=-= Digite lados de um triângulo =-=-=-=-')
lado1 = lerFloat('Lado 1: ', pos=True, erro='Digite um lado válido.')
lado2 = lerFloat('Lado 2: ', pos=True, erro='Digite um lado válido.')
lado3 = lerFloat('Lado 3: ', pos=True, erro='Digite um lado válido.')

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    if lado1 == lado2 == lado3:
        estado = 'equilátero'
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        estado = 'isósceles'
    else:
        estado = 'escalêno'
    print(f'Os lados informados formam um triângulo {estado}.')
else:
    print('Os lados informados não formam um triângulo.')
