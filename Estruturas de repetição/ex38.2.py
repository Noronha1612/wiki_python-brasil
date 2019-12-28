from functions.visual import formatDinheiro
from functions.validação import lerFloat
from datetime import date

anoatual = date.today().year
salario = lerFloat('Digite o salário do funcionário: R$', pos=True, erro='Digite uma quantia válida')
aumento = 0.015
ano = 1996

print('-='*30)
while ano <= anoatual:
    ano += 1
    salario += salario * aumento
    aumento *= 2

print(f'O salário atual vale {formatDinheiro(salario)}')
print('-='*30)
