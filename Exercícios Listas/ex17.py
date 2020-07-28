from functions.validação import lerFloat, media
from functions.visual import tabela, arredondamento

while True:
    nome = input('Digite o nome do atleta: (Digite nenhum nome para parar) ')

    if len(nome) == 0:
        break

    distancias = []

    for distancia in range(1, 6):
        distancias.append(lerFloat(f'Digite a {distancia} de {nome}: ', erro="Digite uma distância válida.", pos=True))
    
    mediaDistancias = arredondamento(media(distancias))
    
    print('\nResultado final:')
    tabela({
        'Atleta': nome,
        'Saltos': ' - '.join(map(str, distancias)),
        'Média': f'{mediaDistancias}m'
    }, alinhar=False, tam=45)

    print('\n\n')

print('Obrigado por usar o meu programa :)')