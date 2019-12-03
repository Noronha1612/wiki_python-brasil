from functions.visual import formatDinheiro
from functions.validação import lerFloat, lerInt

dinheiroh = lerFloat('Quantos R$ você ganha por hora? ', pos=True, erro='Digite uma quantia válida.')
horas = lerInt('Quantas horas, em média, você trabalha por mês? ', erro='Digite uma hora válida e não considere os minutos', pos=True)
salariob = dinheiroh * horas
dados = {
    'Salário bruto' : formatDinheiro(salariob),
    'Imposto de Renda' : formatDinheiro(salariob * 0.11),
    'INSS' : formatDinheiro(salariob * 0.08),
    'Sindicato' : formatDinheiro (salariob * 0.05),
    'Salário líquido' : formatDinheiro(salariob * 0.76)
}

print('-='*20)
for k, v in dados.items():
    print(f'{k:.<25}{v}')
print('-='*20)
