from functions.validação import lerInt, media
from functions.visual import titulo, tabela, arredondamento
from time import sleep

titulo('Analisador de idades')

qtd = lerInt('Quantas pessoas deseja registrar? ', pos=True, erro='Digite uma quantidade válida.')
if qtd == 0:
    print('Encerrando...')
    sleep(1.2)
    exit()

dados = {}
idades = []
for x in range(qtd):
    idade = lerInt(f'Idade da {x + 1}° pessoa: ', pos=True, erro='Digite uma idade válida')
    idades.append(idade)
    dados[f'Idade da {x + 1}° pessoa'] = idade

mediai = arredondamento(media(idades))
dados['Média de idades'] = mediai
if mediai < 25:
    situacao = 'Jovem'
elif mediai < 60:
    situacao = 'Adulta'
else:
    situacao = 'Idosa'
dados['Classificação da turma'] = situacao

tabela(dados, tam=34)
