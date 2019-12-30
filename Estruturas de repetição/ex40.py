from functions.validação import lerInt
from functions.visual import tabela, arredondamento
from time import sleep

somavei = somaaci = maiorvei = menorvei = c = 0
cidades = []
maioresaci = []
menoresaci = []
for x in range(5):
    print('-='*40)
    while True:
        try:
            cod = input(f'Código da {x+1}° cidade: ')
            v = int(cod)
        except:
            print('Digite um código válido')
        else:
            if v > 0:
                break
            print('Digite um código válido')
    qtdvei = lerInt('Quantos carros a passeio passaram nessa cidade no ano de 1999? ', pos=True, erro='Digite uma quantidade válida')
    somavei += qtdvei
    while True:
        acidentes = lerInt('Quantos acidentes nessa cidade no ano de 1999? ', pos=True, erro='Digite uma quantidade válida')
        if acidentes <= qtdvei:
            break
        print('Possibilidade inválida.')
    if x == 0 or acidentes > maiorvei:
        maiorvei = acidentes
    if x == 0 or acidentes < menorvei:
        menorvei = acidentes
    if qtdvei < 2000:
        c += 1
        somaaci += acidentes
    cidades.append([cod, acidentes])
    
    
for v in cidades:
    if v[1] == maiorvei:
        maioresaci.append(v[0])
    if v[1] == menorvei:
        menoresaci.append(v[0])

mediavei = arredondamento(somavei / 5)
mediaaci = arredondamento(somaaci / c)

dados = {
    'Maior índice de acidentes':maiorvei,
    'Menor índice de acidentes':menorvei,
    'Média de veículos nas 5 cidades':mediavei,
    'Média de acidentes nas cidades com menos de 2000 veículos':mediaaci,
    'Código(s) da(s) cidade(s) com maior número de acidentes':  '; '.join(maioresaci),
    'Código(s) da(s) cidade(s) com menor número de acidentes': '; '.join(menoresaci)
}

tabela(dados)
