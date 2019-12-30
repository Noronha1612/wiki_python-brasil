from functions.validação import lerInt
from functions.visual import formatDinheiro
from time import sleep

selec = {
    100:0,
    101:0,
    102:0,
    103:0,
    104:0,
    105:0,
}
produtos = ['Cachorro quente', 'Bauru simples', 'Bauru com ovo', 'Hamburguer', 'Cheeseburguer', 'Refrigerante']
precos = [1.2, 1.3, 1.5, 1.2, 1.3, 1]
produtosselec = []
print("""Opções: 
[100] Cachorro quente....R$1,20
[101] Bauru simples......R$1,30
[102] Bauru com ovo......R$1,50
[103] Hamburguer.........R$1,20
[104] Cheeseburguer......R$1,30
[105] Refrigerante.......R$1,00""")
while True:
    while True:
        op = lerInt('Sua opção: ', erro='Selecione uma opção válida')
        if 100 <= op <= 105:
            break
        print('Selecione uma opção válida')
    
    add = True
    if selec[op] != 0:
        while True:
            esc = input(f'O produto já possui {selec[op]} unidades, deseja adicionar mais unidades? [S/N]').strip().lower()[0]
            if esc in 'sn':
                break
            print('Digite apenas S para "sim" e N para "não"')
        if esc == 'n':
            add = False
    if add:
        while True:
            qtd = lerInt('Qual a quantidade desejada? ', pos=True, erro='Digite uma quantidade válida')
            if qtd != 0:
                break
            print('Não é possivel adicionar 0 quantidades')
        selec[op] += qtd
    while True:
        esc2 = input(f'Deseja pedir algo mais? [S/N] ').strip().lower()[0]
        if esc2 in 'sn':
            break
        print('Digite apenas S para "sim" e N para "não"')
    if esc2 == 'n':
        break

for k, v in selec.items():
    if v != 0:
        produtosselec.append([produtos[k - 100], k])

total = 0
print('Analisando...')
sleep(1.5)
print('-='*17)
for p in produtosselec:
    print(f'{selec[p[1]]}.{p[0]:.<28}{formatDinheiro(precos[p[1] - 100] * selec[p[1]])}')
    total += precos[p[1] - 100] * selec[p[1]]
print(f'{"Valor total":.<30}{formatDinheiro(total)}')
print('-='*17)
