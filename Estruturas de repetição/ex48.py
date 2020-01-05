from functions.validação import lerInt

num = lerInt('Digite um número inteiro positivo: ', pos=True, erro='NÚMERO INTEIRO POSITIVO')
num = str(num)

print(f'O número digitado invertido é: {num[::-1]}')
