from functions.validação import lerInt, lerFloat, media
from functions.visual import formatDinheiro, tabela
from time import sleep

qtd = lerInt("Quantos CD's possui a coleção? ", pos=True, erro='Digite uma quantidade válida')
if qtd == 0:
    print('Encerrando...')
    sleep(1.2)
    exit()

precos = []
for x in range(qtd):
    precos.append(lerFloat(f'Preço do {x + 1}° CD: R$', pos=True, erro='Digite uma quantia válida'))

dados = {
    'Total gasto':formatDinheiro(sum(precos)),
    'Preço médio por CD': formatDinheiro(media(precos))
}  

tabela(dados)
