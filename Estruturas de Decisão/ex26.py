from functions.validação import lerFloat
from functions.visual import titulo, formatDinheiro

titulo('Posto de gasolina')

while True:
    litros = lerFloat('Quantos litros deseja colocar? ', pos=True, erro='Digite uma quantia válida')
    if litros != 0:
        break
    print('Digite algum valor')
print("""Selecione uma das opções:
[G] Gasolina
[A] Álcool""")
while True:
    esc = input('Sua opção: ').strip().lower()[0]
    if esc in 'ga':
        break
    print('Selecione uma opção válida')

gasolina = 2.5
alcool = 1.9
if esc == 'g':
    if litros <= 20:
        precolitro = gasolina * 0.96
    else:
        precolitro = gasolina * 0.94
else:
    if litros <= 20:
        precolitro = alcool * 0.97
    else:
        precolitro = alcool * 0.95

precototal = formatDinheiro(precolitro * litros)

print('-='*15)
print(f'Valor total: {precototal}')
print('-='*15)
