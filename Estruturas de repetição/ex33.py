from functions.validação import media
from functions.visual import arredondamento, tabela, titulo

titulo('Departamento Estadual de Meteorologia')

c = menor = maior = 0
temps = []
while True:
    c += 1
    while True:
        temp = input(f'Temperatura {c} em °C (Deixe em branco para encerrar): ')
        try:
            temp = float(temp)
        except:
            if len(temp) == 0:
                break
            print('Digite um valor válido')
        else:
            if temp >= -273:
                break
            print('Temperatura mínima: -273°C')
    if len(str(temp)) == 0:
        break
    if temp > maior or c == 1:
        maior = temp
    if temp < menor or c == 1:
        menor = temp
    temps.append(temp)
media = arredondamento(media(temps))
if maior % 1 == 0:
    maior = int(maior)
if menor % 1 == 0:
    menor = int(menor)
if media % 1 == 0:
    media = int(media)
dados = {
    'Maior temperatura registrada': f'{maior}°C',
    'Menor temperatura registrada': f'{menor}°C',
    'Média de temperatura': f'{media}°C'
}

tabela(dados)
