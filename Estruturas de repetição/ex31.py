from functions.validação import lerFloat
from functions.visual import formatDinheiro, tabela, titulo
from time import sleep

titulo('Lojas Tabajara')

c = soma = 0
dados = {}
while True:
    c += 1
    p = lerFloat(f'Preço do {c}° produto (Digite 0 para encerrar): R$', pos=True, erro='Digite uma quantidade válida')
    if c == 1 and p == 0:
        print('Nenhum produto registrado, encerrando...')
        sleep(1.2)
        exit()
    if p == 0:
        break
    dados[f'Produto {c}'] = formatDinheiro(p)
    soma += p
dados['Total'] = formatDinheiro(soma)
print('Valor total: ' + dados['Total'])
while True:
    quantia = lerFloat('Quantia paga pelo cliente: R$', pos=True, erro='Digite uma quantia válida')
    if quantia > soma:
        dados['Dinheiro'] = formatDinheiro(quantia)
        break
    print('Quantia insuficiente.')
if quantia - soma != 0:
    dados['Troco'] = formatDinheiro(quantia - soma)

print('Analisando...')
sleep(1.2)
tabela(dados)