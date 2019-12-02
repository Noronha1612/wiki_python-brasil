from functions.validação import lerFloat
from functions.visual import formatDinheiro, arredondamento
from math import ceil

#Declaração de variáveis
valores = {}
peso = lerFloat('Peso em Kg: ')
val = 0 #Variável apenas para validação na "operação ternária"
if peso > 50:
    excesso = arredondamento(peso - 50)
    multa = formatDinheiro(ceil(excesso) * 4)
    val += 1
else:
    excesso = 'Dentro do regulamento'
    multa = 'Inexistente'
valores['Peso'] = str(peso) + 'Kg'
valores['Excesso'] = (f'{excesso}Kg' if val == 1 else excesso) #"Operação ternária"
valores['Multa'] = multa

#Impressão da tabela
print('-='*20)
for k, v in valores.items():
    print(f'{k}: {v}')
print('-='*20)
