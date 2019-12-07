from functions.validação import lerFloat
from functions.visual import formatDinheiro, tabela, arredondamento

salarioini = lerFloat('Digite seu sálario: ', pos=True, erro='Digite um salário válido.')

if salarioini <= 280:
    aumento = 0.2
elif salarioini <= 700:
    aumento = 0.15
elif salarioini <= 1500:
    aumento = 0.1
else:
    aumento = 0.05

salariofinal = salarioini + salarioini * aumento

valores = {
    'Salário inicial': formatDinheiro(salarioini),
    'Aumento percentual': str(arredondamento(aumento*100)) + '%',
    'Aumento em dinheiro': formatDinheiro(salarioini * aumento),
    'Salário final': formatDinheiro(salariofinal)
}

tabela(valores)
