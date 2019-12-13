from functions.validação import lerInt

num = lerInt('Digite um número inteiro: ', erro='\33[1;31mINTEIRO...\33[m')

par = False
if num % 2 == 0:
    par = True

if num == 0:
    print('O número 0 é NULO')
elif par:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')
