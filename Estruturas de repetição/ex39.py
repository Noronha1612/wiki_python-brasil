from functions.validação import lerInt
from functions.visual import tabela

maior = menor = 0
nmrs = []
maioresa = []
menoresa = []
for x in range(10):
    while True:
        try:
            num = input(f'Número do {x+1}° aluno: ')
            v = int(num)
        except:
            print('Digite um número válido')
        else:
            if v > 0:
                break
            print('Digite um número válido')
    
    while True:
        alt = lerInt('Digite sua altura em cm: ', pos=True, erro='Digite uma altura válida')
        if 50 < alt < 300:
            break
        print('Digite uma altura válida')
    if alt > maior:
        maior = alt
    if x == 0 or alt < menor:
        menor = alt
    nmrs.append([num, alt])

for v in nmrs:
    if v[1] == maior:
        maioresa.append(v[0])
    if v[1] == menor:
        menoresa.append(v[0])

dados = {
    'Maior altura registrada': f'{maior} cm',
    'Menor altura registrada': f'{menor} cm',
    'Número(s) da(s) pessoa(s) mais alta': f'{"; ".join(maioresa)} cm',
    'Número(s) da(s) pessoa(s) mais baixa': f'{"; ".join(menoresa)} cm'
}

tabela(dados, tam=48)
