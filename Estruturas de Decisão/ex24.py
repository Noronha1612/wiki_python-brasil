from functions.validação import lerFloat, lerInt
from functions.visual import titulo, arredondamento
from time import sleep

titulo('Analisador de dados')

num1 = lerFloat('Número 1: ')
num2 = lerFloat('Número 2: ')

print("""O que deseja fazer com esses números?
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir""")

opcoes = [1, 2, 3, 4]
while True:
    opcao = lerInt('Sua opção: ', erro='Digite uma opção válida')
    if opcao in opcoes:
        break
    print('Digite uma opção válida')

if opcao == 1:
    res = num1 + num2
elif opcao == 2:
    res = num1 - num2
elif opcao == 3:
    res = num1 * num2
else:
    res = num1 / num2

inteiro = False
positivo = False
par = False
if res % 1 == 0:
    inteiro = True
if res > 0:
    positivo = True
if res % 2 == 0:
    par = True

print('-='*15)
print(f'Resultado: {arredondamento(res)}')
print('Analisando...')
sleep(1.5)
if res == 0:
    print('O valor não é par nem ímpar, é nulo')
elif inteiro == False:
    print('Não é possível análisar se esse número é par ou ímpar')
elif par:
    print('O valor é par.')
else:
    print('O valor é ímpar.')
if res == 0:
    print('O valor não é positivo nem negativo, é núlo')
elif positivo:
    print('O valor é positivo.')
else:
    print('O valor é negativo.')
if inteiro:
    print('O valor é inteiro')
else:
    print('O valor é decimal')
print('-='*15)
