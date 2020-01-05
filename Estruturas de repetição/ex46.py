from functions.validação import lerFloat
from functions.visual import titulo, tabela, arredondamento
from time import sleep

titulo('Salto em distância')

atletas = []
while True:
    saltos = []
    c = False
    nome = input('Nome do atleta (deixa em branco para encerrar o programa): ').strip().upper()
    if nome == "":
        break
    else:
        for p in atletas:
            if p[0] == nome:
                c = True
                print('Esse nome ja foi registrado')
        if c:
            continue
    for x in range(5):
        saltos.append(lerFloat(f'Distância do {x + 1}° Salto em metros: '))
    saltos.sort()
    tabela({
        'Melhor salto': f'{saltos[4]}m',
        'Pior salto': f'{saltos[0]}m',
        'Média dos demais saltos': f'{arredondamento(sum(saltos[1:4]) / 3)}'
    }, tam=30)
    atletas.append([nome, arredondamento(sum(saltos[1:4]) / 3)])

if len(atletas) == 0:
    print('Nenhum atleta registrado.')
    print('Encerrando...')
    sleep(1.3)
    exit()

print('Analisando...')
sleep(1.5)
print('-='*25)
print('Médias')
for a in atletas:
    print(f'{a[0]}: {a[1]}m')
print('-='*25)
