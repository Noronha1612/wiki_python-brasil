from functions.validação import lerFloat
while True:
    altura = lerFloat('Digite sua altura em metros: ')
    if 0.5 <= altura <= 3:
        break
    print('Digite uma altura em metros válida.')
print(f'Seu peso ideal é de {(72.7 * altura) - 58:.1f}Kg')
