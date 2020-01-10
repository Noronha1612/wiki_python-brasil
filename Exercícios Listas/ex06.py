from functions.validação import lerNota

alunos = []

for x in range(10):
    notas = []
    for y in range(4):
        notas.append(lerNota(f'{y + 1}° Nota do {x + 1}° aluno: '))
    media = sum(notas) / len(notas)
    alunos.append(media)
    print('Média de aluno registada')

aprovados = 0
for a in alunos:
    if a >= 7:
        aprovados += 1

print('-='*25)
print(f'Quantidade de alunos aprovados com média maior ou igual a 7: {aprovados} alunos')
print('-='*25)
