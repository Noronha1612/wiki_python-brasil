from functions.validação import lerFloat

num1 = lerFloat('Digite um número: ')
maior = num1
num2 = lerFloat('Digite outro número: ')
if num2 > maior:
    maior = num2
num3 = lerFloat('Digite o último número: ')
if num3 > maior:
    maior = num3

print(f'O maior valor digitado foi {maior}')
