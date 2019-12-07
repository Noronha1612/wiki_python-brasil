from functions.validação import lerInt

dias = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']
while True:
    dia = lerInt('Digite um número de 1 a 7: ')
    if 0 < dia <= 7:
        break
    print('NÚMERO DE 1 A 7')

print(f'O dia {dia} corresponde a {dias[dia - 1]}')
