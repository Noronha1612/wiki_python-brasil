from functions.validação import lerFloat
from functions.visual import tabela

lista = []

for x in range(3):
    lista.append(lerFloat("Digite: "))

tabela({
    "Números digitados": lista
})
