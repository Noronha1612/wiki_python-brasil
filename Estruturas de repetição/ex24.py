from functions.validação import lerNota, lerInt
from functions.visual import titulo, arredondamento, tabela

titulo('Calculo de média')

qtd = lerInt('Quantas notas deseja analisar? ', pos=True, erro='Digite uma quantidade válida')
if qtd == 0:
    print('Encerrando...')
    exit()

dados = {}
soma = c = 0
for x in range(qtd):
    nota = lerNota(f'{x + 1}° Nota: ')
    soma += nota
    c += 1
    dados[f'Nota {x + 1}'] = nota

dados['Média'] = arredondamento(soma / c)

tabela(dados, tam=12)
