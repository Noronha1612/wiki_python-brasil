from functions.validação import lerFloat

num1 = lerFloat('Número 1: ')
num2 = lerFloat('Número 2: ')

print(f'Entre {num1} e {num2}, o maior valor é {num1 if num1 > num2 else num2}')
