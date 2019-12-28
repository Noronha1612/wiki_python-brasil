from functions.validação import lerFloat
from functions.visual import formatDinheiro
from datetime import date

ano = 1995
atual = date.today().year
salario = lerFloat('Salário inicial: R$', pos=True, erro='Digite uma quantia válida')
aumento = 0.015

while ano != atual:
    ano += 1
    salario += salario * aumento
    aumento *= 2

print('Novo salário: ' + formatDinheiro(salario))
