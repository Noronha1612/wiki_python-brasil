meses = {1: 'Janeiro',
2: 'Fevereiro',
3: 'Março',
4: 'Abril',
5: 'Maio',
6: 'Junho',
7: 'Julho',
8: 'Agosto',
9: 'Setembro',
10: 'Outubro',
11: 'Novembro',
12: 'Dezembro'}
mes31 = [1, 3, 5, 7, 8, 10, 12]
mes30 = [4, 6, 9, 11]

while True:
    data = input('Digite uma data no formato dd/mm/aaaa: ')
    try:
        data = data.split(sep='/')
        dia = data[0]
        mes = data[1]
        ano = data[2]
    except:
        print('Formato inválido.')
    else:
        try:
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
            if dia < 0:
                dia *= -1
            if mes < 0:
                mes *= -1
        except:
            print('Digite apenas números inteiros e barras.')
        else:
            break

if mes <= 12:
    data = f'{dia} de {meses[mes]} de {ano}'
    if mes in mes31:
        if dia <= 31:
            print(f'A data {data} é válida')
        else:
            print(f'A data {data} é inválida')
    elif mes in mes30:
        if dia <= 30:
            print(f'A data {data} é válida')
        else:
            print(f'A data {data} é inválida')
    else:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if dia <= 29:
                print(f'A data {data} é válida')
            else:
                print(f'A data {data} é inválida')
        else:
            if dia <= 28:
                print(f'A data {data} é válida')
            else:
                print(f'A data {data} é inválida')
else:
    print('Data inválida')
    
