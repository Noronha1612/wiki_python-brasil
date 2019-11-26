from functions.validação import lerFloat
from functions.visual import arredondamento
opções = ['°F', '°C'] #Lista com siglas usadas na formatação da resposta
print("""\33[1;32mSuas opções: 
[1] Celsius -> Farenheit
[2] Farenheit -> Celsius\33[m""")
while True:
    esc = input('\33[1;34mSua opção: \33[m') #Seleciona as opções [1] ou [2] com tratamento de erro
    if esc == '1' or esc == '2':
        break
    print('Selecione uma opção válida.')
if esc == '1':
    valor = lerFloat('Quantos °C queres transformar pra Farenheit? ')
    res = arredondamento(1.8 * valor + 32) #Formula para transformação de °C para °F (°C/5 = (°F-32)/9)
else:
    valor = lerFloat('Quantos °F queres transformar pra Celsius? ') 
    res = arredondamento((valor - 32)/1.8) #Formula para transformação de °F para °C (°C/5 = (°F-32)/9)
print(f'{valor}{opções[int(esc)-2]} valem {res}{opções[int(esc)-1]}') #Valores numericos seguidos de indexações da lista "opções"
#Mesmo código do exemplo 09