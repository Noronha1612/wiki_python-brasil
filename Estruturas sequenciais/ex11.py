from functions.validação import lerFloat, lerInt
from functions.visual import arredondamento
opções = ['int', 'int', 'float']
numeros = []
while len(opções) != 0:
    if 'int' in opções and 'float' in opções:
        num = lerFloat('Digite um númeiro inteiro ou real: ')
        numeros.append(num)
        if num % 1 == 0:
            opções.remove('int')
        else:
            opções.remove('float')
    elif 'int' in opções:
        num = lerInt('Digite um número inteiro: ')
        numeros.append(num)
        opções.remove('int')
    else:
        while True:
            num = lerFloat('Digite um número real: ')
            if num % 1 != 0:
                numeros.append(num)
                opções.remove('float')
                break
            print('Digite um valor REAL.')
print('-='*42)
print(f"""a) O produto do dobro do primeiro com a metade do segundo: ({numeros[0]} * 2) * ({numeros[1]} / 2) = {arredondamento((numeros[0]*2)*(numeros[1]/2))}
b) A soma do triplo do primeiro com o terceiro: ({numeros[0]} * 3) + {numeros[2]} = {arredondamento((numeros[0] * 3) + numeros[2])}
c) O terceiro elevado ao cubo: {numeros[2]}³ = {arredondamento(numeros[2]**4)}""")
print('-='*42)
