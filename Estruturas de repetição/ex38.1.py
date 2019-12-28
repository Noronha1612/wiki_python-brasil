from functions.visual import formatDinheiro
from datetime import date

ano = 1995
atual = date.today().year
salario = 1000
aumento = 0.015

while ano != atual:
    ano += 1
    salario += salario * aumento
    aumento *= 2

print('Novo salário: ' + formatDinheiro(salario))
