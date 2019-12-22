from functions.validação import lerInt
from functions.visual import titulo

titulo('ELEIÇÕES')

qtd = lerInt('Quantas pessoas votarão? ', pos=True, erro='Digite uma quantidade válida.')
if qtd == 0:
    print('Eleições canceladas por falta de eleitores')
    exit()

candidatos = {'p': 0, 'c': 0, 'f': 0}
print('-='*10)
print("""Candidatos:
[C] Caique
[F] Fernando
[P] Pedro""")
print('-='*10)
for x in range(qtd):
    while True:
        try:
            esc = input(f'Candidato n° {x + 1}, selecione sua opção: ').strip().lower()[0]
        except:
            print('Selecione uma opção válida.')
        else:
            if esc in candidatos.keys():
                break
            print('Selecione uma opção válida.')
    candidatos[esc] += 1

pontuacoes = []
for v in candidatos.values():
    pontuacoes.append(v)
pontuacoes.sort(reverse=True)
ranking = []
while len(pontuacoes) != 0:
    for k, v in candidatos.items():
        if v == pontuacoes[0]:
            if k == 'p':
                ranking.append(['Pedro', v])
            elif k == 'c':
                ranking.append(['Caique', v])
            else:
                ranking.append(['Fernando', v])
            pontuacoes.pop(0)
            del candidatos[k]
            break

print('~'*50)
for l, p in enumerate(ranking):
    plural = True
    if p[1] == 1:
        plural = False
    print(f'{l + 1}° Lugar - {p[0]} com {p[1]} {"votos" if plural == True else "voto"}')
print('~'*50)
