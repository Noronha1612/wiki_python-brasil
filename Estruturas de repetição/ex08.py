from functions.validação import lerFloat
from functions.visual import arredondamento, tabela

numeros = []
for x in range(5):
    numeros.append(lerFloat(f'{x + 1}° Número: '))

soma = sum(numeros)
media = arredondamento(soma / len(numeros))
dados = {
    'Soma':arredondamento(soma),
    'Média':media
}

tabela(dados)
