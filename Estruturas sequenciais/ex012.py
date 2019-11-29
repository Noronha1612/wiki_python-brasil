from functions.validação import lerOnlyFloat
altura = lerOnlyFloat('Digite sua altura em métros: ', 'Em metros! ex(1,72)')
print(f'Seu peso ideal é de {(72.7 * altura) - 58:.1f}Kg')
