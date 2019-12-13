from functions.visual import tabela, formatDinheiro, titulo
from functions.validação import lerFloat

titulo('Hipermercado Tabajara')

carnes = {
    'F': 'Filé duplo',
    'A': 'Alcantra',
    'P': 'Picanha'
}
print("""Selecione uma opção de carne:
[F] Filé duplo
[A] Alcantra
[P] Picanha""")
while True:
    esc = input('Sua opção: ').upper().strip()[0]
    if esc in 'FAP':
        break
    print('Selecione uma opção válida')

while True:
    quantidade = lerFloat('Quantos Kg deseja comprar? ', pos=True, erro='Digite uma quantidade válida')
    if quantidade != 0:
        break
    print('A quantidade não pode ser 0Kg')

if esc == 'F':
    if quantidade > 5:
        precokg = 5.8
    else:
        precokg = 4.9
elif esc == 'A':
    if quantidade > 5:
        precokg = 6.8
    else:
        precokg = 5.9
else:
    if quantidade > 5:
        precokg = 7.8
    else:
        precokg = 6.9

precototal = precokg * quantidade

formaspagamento = {
    'B': 'Boleto bancário',
    'C': 'Cartão Tabajara',
    'D': 'Dinheiro'
}
print("""Selecione sua forma de pagamento: 
[B] Boleto bancário
[C] Cartão Tabajara
[D] Dinheiro""")
while True:
    esc2 = input('Sua opção: ').strip().upper()[0]
    if esc2 in 'BCD':
        break
    print('Selecione uma opção válida')

desconto = '0%'
precopagar = precototal
if esc2 == 'C':
    precopagar = precototal * 0.95
    desconto = '5%'

dados = {
    'Tipo de carne': carnes[esc],
    'Quantidade': f'{quantidade}Kg',
    'Tipo de pagamento': formaspagamento[esc2],
    'Preço total': formatDinheiro(precototal),
    'Desconto': desconto,
    'Preço a se pagar': formatDinheiro(precopagar)
}

tabela(dados)
