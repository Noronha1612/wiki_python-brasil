from functions.validação import lerFloat, lerInt
from functions.visual import tabela
from time import sleep

maior = menor = 0
alturas = []
numeros = []
maioresalt = []
menoresalt = []
for x in range(10):
    while True:
        try:
            num = input(f'Número do {x +1}° aluno: ')
            v = int(num)
        except:
            print('Digite um número inteiro válido')
        else:
            if 0 < v < 100 and num not in numeros:
                break
            if num in numeros:
                print('Valor repetido, digite outro')
            else:
                print('Digite um número de 1 a 100 inteiro')
    while True:
        alt = lerFloat(f'Altura do {x +1}° aluno em metros: ', pos=True, erro='Digite uma altura válida')
        if 0.5 < alt < 3:
            break
        print('Digite uma altura em METROS válida')
    if x == 0 or alt > maior:
        maior = alt
    if x == 0 or alt < menor:
        menor = alt
    alturas.append([num, alt])
    numeros.append(num)
for alt in alturas:
    if alt[1] == maior:
        maioresalt.append(alt[0])
    if alt[1] == menor:
        menoresalt.append(alt[0])

dados = {
    'Maior altura registrada': f'{maior if maior % 1 == 0 else round(maior, 2)} metros',
    'Menor altura registrada': f'{menor if menor % 1 == 0 else round(menor, 2)} metros',
    'Número(s) da(s) Pessoa(s) mais alta(s)': '; '.join(maioresalt),
    'Número(s) da(s) Pessoa(s) mais baixa(s)': '; '.join(menoresalt)
}

print('Analisando...')
sleep(1.2)
tabela(dados)
