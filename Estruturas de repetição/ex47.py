from functions.validação import lerNota
from functions.visual import tabela, arredondamento, titulo
from time import sleep

titulo('Competição de ginástica')

nome = input('Nome do atleta: ').strip()
if nome == "":
    print('Nenhum atleta informado...')
    exit()

notas = []
for x in range(7):
    notas.append(lerNota(f'Nota do {x + 1}° jurado: '))
notas.sort()
maior = notas[len(notas) - 1]
menor = notas[0]

media = arredondamento(sum(notas[1:6]) / 5)

print('Analisando...')
sleep(1.1)
dados = {
    'Atleta': nome,
    'Maior nota': maior,
    'Menor nota': menor,
    'Média de notas': media
}

tabela(dados)
