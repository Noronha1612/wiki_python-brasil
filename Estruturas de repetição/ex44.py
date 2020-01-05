from functions.validação import lerInt
from functions.visual import titulo, arredondamento
from time import sleep

candidatos = [[1, 'Pedro', 0], [2, 'José', 0], [3, 'Fernando', 0], [4, 'Lucas', 0], [5, 'voto nulo', 0], [6, 'voto em branco', 0]]
qtdvotos = []
titulo('Eleições')
print("""Candidatos
[1] Pedro
[2] José
[3] Fernando
[4] Lucas
[5] Voto nulo
[6] Voto em branco""")
while True:
    while True:
        esc = lerInt('Sua opção: (digite "0" para encerrar a eleição) ', erro='Selecione uma opção válida')
        if 0 <= esc <= 6:
            break
        print('Selecione uma opção válida')
    if esc == 0:
        break
    else:
        for c in candidatos:
            if c[0] == esc:
                c[2] += 1
        print('Dado registrado com sucesso')

soma = 0
for c in candidatos:
    soma += c[2]
for c in candidatos:
    qtdvotos.append(c[2])
qtdvotos.sort(reverse=True)
ranking = []
while len(qtdvotos) != 0:
    for c in candidatos:
        if c[2] == qtdvotos[0]:
            if c[1] != 'voto em branco' and c[1] != 'voto nulo':
                ranking.append([c[1], c[2]])
                candidatos.remove(c)
                break
    qtdvotos.pop(0)

print('Analisando...')
sleep(1.5)
print('-='*28)
for i, v in enumerate(ranking):
    print(f'{i + 1}°. {v[0]:<10}com {v[1]} {"voto" if v[1] == 1 else "votos"}')
print(f'Quantidade de votos nulos: {candidatos[0][2]} {"voto" if candidatos[0][2] == 1 else "votos"}')
print(f'Quantidade de votos em branco: {candidatos[1][2]} {"voto" if candidatos[1][2] == 1 else "votos"}')
print(f'Porcentagem de votos nulos sobre o total de votos: {arredondamento(100 *(candidatos[0][2] / soma))}%')
print(f'Porcentagem de votos em branco sobre o total de votos: {arredondamento(100 * (candidatos[1][2] / soma))}%')
print('-='*28)
