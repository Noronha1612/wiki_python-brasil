from functions.validação import lerHoraPorDia, lerFloat
from functions.visual import tabela, arredondamento, formatDinheiro

#Declaração de variáveis
dados = {}
valorhora = lerFloat('Quanto você ganha por hora? ', pos=True, erro='Digite uma quântia válida')
hora = lerHoraPorDia('Quantas horas, em média, você trabalha por dia? (Desconsidere os minutos) ', erro='Digite uma hora válida')
salario = valorhora * hora * 30
inss = salario * 0.03
fgts = salario * 0.11
if salario <= 900:
    impostoderenda = 0
elif salario <= 1500:
    impostoderenda = salario * 0.05
elif salario <= 2500:
    impostoderenda = salario * 0.1
else:
    impostoderenda = salario * 0.2
descontos = impostoderenda + inss
salarioliquido = salario - descontos

#Adicionando valores ao dicionário "dados"
dados['Salário bruto'] = formatDinheiro(salario)
dados['INSS'] = formatDinheiro(inss)
dados['Imposto de Renda'] = formatDinheiro(impostoderenda)
dados['FGTS'] = formatDinheiro(fgts)
dados['Total de descontos'] = formatDinheiro(descontos)
dados['Salário líquido'] = formatDinheiro(salarioliquido)

tabela(dados, alinhar=True)
