from functions.validação import lerFloat 

num = lerFloat('Digite um número: ')
if num > 0:
    condicao = 'positivo'
elif num == 0:
    condicao = 'nulo'
else:
    condicao = 'negativo'

print(f'O valor {num} é um valor {condicao}.')