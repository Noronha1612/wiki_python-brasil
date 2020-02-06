from functions.validação import lerFloat
from functions.visual import tabela

v1 = []
v2 = []
v3 = []
v4 = []

for x in range(10):
    v1.append(lerFloat(f"Digite o {x + 1}° número do 1° vetor: "))

print("\n")

for y in range(10):
    v2.append(lerFloat(f"Digite o {y + 1}° número do 2° vetor: "))

print("\n")

for z in range(10):
    v3.append(lerFloat(f"Digite o {z + 1}° número do 3° vetor: "))

for i, v in enumerate(v1):
    v4.append(v)
    v4.append(v2[i])
    v4.append(v3[i])

tabela({
    "Elementos do 1° vetor": v1,
    "Elementos do 2° vetor": v2,
    "Elementos do 3° vetor": v3,
    "Elementos do 4° vetor": v4
}, tam=154)

