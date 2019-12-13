from functions.validação import lerNota
from functions.visual import arredondamento

notas = []
for x in range(3):
    notas.append(lerNota(f'Nota {x + 1}: '))

media = arredondamento(sum(notas) / len(notas))
if media < 7:
    situacao = 'Reprovado(a)'
elif media < 10:
    situacao = 'Aprovado(a)'
else:
    situacao = 'Aprovado(a) com distinção'

print('-='*15)
print(f'Média: {media}')
print(f'Situação: {situacao}')
print('-='*15)
