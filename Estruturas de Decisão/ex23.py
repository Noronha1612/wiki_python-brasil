from functions.validação import lerFloat

num = lerFloat('Digite um valor: ')

inteiro = False
if num % 1 == 0:
    inteiro = True

print(f'O valor {num} é ', end='')
if inteiro:
    print('INTEIRO')
else:
    print('DECIMAL')
