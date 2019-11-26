from functions.validação import lerNota
from functions.visual import arredondamento
notas = [] #Lista onde será guardada as notas
for nota in range(4):
    notas.append(lerNota(f'{nota + 1}° Nota: ')) #Adiciona uma nota a lista "notas"
media = arredondamento(sum(notas) / len(notas)) #tira a média das notas / se tiver muitas casas flutuantes, será arredondado
print('~'*23)
notas.sort(reverse=True) #Arruma a lista "notas" em ordem decrescente
for num, nota in enumerate(notas):
    print(f'{num+1}° Melhor nota: {nota}') #Ranking
print(f'Média: {media}')
print('~'*23)
