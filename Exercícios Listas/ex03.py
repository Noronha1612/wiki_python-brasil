from functions.validação import lerNota
from functions.visual import arredondamento, tabela

dados = {}
notas = []
for x in range(4):
    nota = lerNota(f'Nota {x + 1}: ')
    notas.append(nota)
    dados[f"Nota {x+1}"] = nota

media = arredondamento(sum(notas) / len(notas))
dados['Média'] = media

tabela(dados, tam=18)
