from functions.validação import lerFloat
from functions.visual import titulo, formatDinheiro, tabela, arredondamento

kgmaca = lerFloat('Kg de maçã: ', pos=True, erro='Digite uma quantidade válida')
kgmorango = lerFloat('Kg de morango: ', pos=True, erro='Digite uma quantidade válida')
kgtotal = kgmorango + kgmaca

precomaca = 1.8
precomorango = 2.5
if kgmorango > 5:
    precomorango = 2.2
if kgmaca > 5:
    precomaca = 1.5
precototal = precomaca * kgmaca + precomorango * kgmorango

dados = {
    'Preço total': formatDinheiro(precototal),
    'Peso total': f'{arredondamento(kgtotal)}Kg'
}
if kgtotal > 8 or precototal > 25:
    precototal *= 0.9
    dados['Desconto'] = '10%'
    dados['Preço total'] = formatDinheiro(precototal)

tabela(dados)
