from functions.validação import lerInt
from functions.visual import arredondamento, tabela
from time import sleep

nturmas = lerInt('Quantas turmas deseja analisar? ', pos=True, erro='Digite uma quantidade válida')
if nturmas == 0:
    print('Encerrando...')
    sleep(1.2)
    exit()

soma = 0
dados = {}
for x in range(nturmas):
    while True:
        qtd = lerInt(f'Quantas alunos na turma {x + 1}? ', pos=True, erro='Digite uma quantidade válida')
        if qtd <= 40:
            break
        print('Não é possivel ter mais que 40 pessoas em uma turma')
    soma += qtd
    dados[f'Turma {x + 1}'] = f'{qtd} pessoas'

media = arredondamento(soma / nturmas)
dados['Média de alunos por turma'] = f'{media} pessoas'

print('Analisando...')
sleep(1.2)

tabela(dados, tam=40)
