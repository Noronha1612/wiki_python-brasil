from functions.validação import lerInt
from functions.visual import tabela


def calculatePercentage(playerV: int, totalV: int):
    percentage = 100 * (playerV / totalV)

    return f'{percentage:.1f}%'


def sortOrder(e):
    return e[1]


players = []

totalVotes = 0

while True:
    while True:
        player = lerInt('Número do jogador (0=fim): ', erro='Informe um valor entre 1 e 23 ou 0 para sair!', pos=True)

        if 0 <= player <= 23:
            break
        
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    
    if player == 0:
        break

    alreadyExist = False

    for p in players:
        if p[0] == player:
            alreadyExist = True

    if not(alreadyExist):
        players.append([ player, 1 ])
    else:
        for p in players:
            if p[0] == player:
                p[1] += 1
    
    totalVotes += 1

for p in players:
    p.append(calculatePercentage(p[1], totalVotes))
    
print('\nResultado da votação:\n')

print(f'Foram computados {totalVotes} votos\n')

print(f'{"Jogador/votos":<30}%')

melhor = [0, 0, 0]

players.sort(key=sortOrder, reverse=True)

for p in players:
    tabela({
        f'{p[0]}/{p[1]}': p[2]
    }, alinhar=True, title=False)

    if p[1] > melhor[1]:
        melhor = p

print(f'\nO melhor jogador foi o número {melhor[0]}, com {melhor[1]} {"voto" if melhor[1] == 1 else "votos"}, correspondendo a {melhor[2]} do total de votos.')