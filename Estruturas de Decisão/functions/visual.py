def arredondamento(num):
    res = num
    if len(str(res)[str(res).find('.'):]) >= 5:
        res = round(res, 2)
        return res
    if res % 1 == 0:
        res = int(res)
        return res
    elif res % 0.1 == 0:
        res = round(res, 1)
        return res
    else:
        return res


def formatDinheiro(num):
    res = f'R${num:.2f}'
    res = res.replace('.',',')
    return res


def tabela(dicio, alinhar=False):
    print('-='*20)
    if alinhar:
        for k, v in dicio.items():
            print(f'{k:.<30}{v}')
    else:
        for k, v in dicio.items():
            print(f'{k}: {v}')
    print('-='*20)
