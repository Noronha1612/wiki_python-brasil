from functions.validação import lerInt
from functions.visual import tabela

A = []

for x in range(10):
    A.append(lerInt(f'Digite o {x + 1}° número: '))
    print()

soma = 0
for v in A:
    soma += v**2

for y in range(len(A)):
    A[y] = str(A[y])

tabela({
    'Valores digitados': '; '.join(A),
    'Soma dos quadrados desses valores': soma
}, tam=56)
