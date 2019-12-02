from functions.validação import lerFloat, lerInt
from functions.visual import formatDinheiro
qtdphr = lerFloat('Quanto você ganha por hora (em R$)? ') #ler a quantidade de dinheiro por hora
qtddhr = lerInt('Quantas horas, em média, você trabalha por mês? ')
print('~'*40)
print(f'Você ganha, em média, {formatDinheiro(qtdphr*qtddhr)} por mês')
print('~'*40)
