from functions.validação import lerFloat, lerInt, media
from functions.visual import tabela, titulo, arredondamento
from time import sleep

titulo('Senso altura e peso')

pessoas = {}
maiora = menora = maiorp = menorp = c = 0
alturas = []
pesos = []
while True:
    while True:
        cod = input('Digite seu código (Digite 0 para encerrar): ')
        try:
            v = int(cod)
        except:
            print('Digite um código válido.')
        else:
            if v >= 0:
                break
    if int(cod) == 0:
        break
    c += 1
    while True:
        altura = lerFloat('Digite sua altura em metros: ', pos=True, erro='Digite uma altura válida')
        if 0.5 < altura < 2.8:
            break
        print('Digite uma altura em metros válida')
    if altura > maiora or c == 1:
        maiora = altura
    if altura < menora or c == 1:
        menora = altura
    
    while True:
        peso = lerFloat('Digite seu peso em Kg: ', pos=True, erro='Digite um peso válido')
        if 10 < peso < 350:
            break
        print('Digite um peso válido')
    if peso > maiorp or c == 1:
        maiorp = peso
    if peso < menorp or c == 1:
        menorp = peso
    pessoas[cod] = [altura, peso]
    alturas.append(altura)
    pesos.append(peso)

if len(pessoas) == 0:
    print('Nenhuma pessoa registrada')
    print('Encerrando...')
    sleep(1.2)
    exit()

mediaa = arredondamento(media(alturas))
mediap = arredondamento(media(pesos))
maioresa = []
menoresa = []
maioresp = []
menoresp = []
for k, v in pessoas.items():
    if v[0] == maiora:
        maioresa.append(k)
    if v[0] == menora:
        menoresa.append(k)
    if v[1] == maiorp:
        maioresp.append(k)
    if v[1] == menorp:
        menoresp.append(k)

dados = {
    'Média de altura': mediaa,
    'Média de peso': mediap,
    'Código da(s) pessoa(S) com maior altura': '; '.join(maioresa),
    'Código da(s) pessoa(S) com menor altura': '; '.join(menoresa),
    'Código da(s) pessoa(S) com maior peso': '; '.join(maioresp),
    'Código da(s) pessoa(S) com menor peso': '; '.join(menoresp),
}

print('Analisando...')
sleep(1.2)
tabela(dados, tam=50)
