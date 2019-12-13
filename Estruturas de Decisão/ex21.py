from functions.validação import lerFloat
from time import sleep

while True:
    quantia = lerFloat('Valor a ser sacado: R$', pos=True, erro='Digite uma quantia válida.')
    if quantia > 600:
        print('Valor máximo: R$600,00')
    elif quantia <= 0:
        print('Valor mínimo: R$1,00')
    elif quantia % 1 != 0:
        print('Não é possivel sacar centavos... Digite um valor inteiro')
    else:
        break

notas100 = quantia // 100
quantia -= notas100 * 100

notas50 = quantia // 50
quantia -= notas50 * 50

notas10 = quantia // 10
quantia -= notas10 * 10

notas5 = quantia // 5
quantia -= notas5 * 5

notas1 = quantia

notas = {
    'Notas de R$100,00':notas100,
    'Notas de R$50,00':notas50,
    'Notas de R$10,00':notas10,
    'Notas de R$5,00':notas5,
    'Notas de R$1,00':notas1
}

print('-='*15)
print('SACANDO...')
sleep(1)
for k, v in notas.items():
    if v != 0:
        print(f'{k}: {v}')
print('-='*15)
