from functions.validação import lerFloat, lerInt
from functions.visual import formatDinheiro
from time import sleep

divida = lerFloat('Valor da dívida: R$', pos=True, erro='Digite uma quantia válida')
if divida == 0:
    print('Nenhuma dívida registrada')
    print('Programa encerrado')
    exit()

while True:
    parcelas = lerInt('Quantas parcelas deseja pagar? ', pos=True, erro='Digite uma quantidade válida')
    if parcelas > 0:
        break
    print('Digite uma quantidade válida')

if parcelas < 3:
    juros = 0
else:
    juros = 5 + 5 * (parcelas // 3)

total = divida + (divida * (juros / 100))

print('Analisando...')
sleep(1.5)
print(f'{"Valor da dívida":<30}{"Valor do juros":<30}{"Quantidade de parcelas":<30}{"Valor da parcela":<30}{"Valor total"}')
print('-='*76)
print(f'{formatDinheiro(divida):<30}{formatDinheiro(divida * (juros / 100)):<30}{parcelas:<30}{formatDinheiro(total / parcelas):<30}{formatDinheiro(total)}')
