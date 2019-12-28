from functions.visual import formatDinheiro
from datetime import date

anoatual = date.today().year
salario = 1000
aumento = 0.015
ano = 1996

while ano <= anoatual:
    ano += 1
    salario += salario * aumento
    aumento *= 2

print(f'O salário atual vale {formatDinheiro(salario)}')
