def arredondamento(num, inteiro=False):
    if inteiro:
        return int(round(num, 0))
    res = num
    if len(str(res)[str(res).find('.'):]) >= 4:
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


def tabela(dicio, alinhar=False, tam=36, title=True):
    if title:
        print('TABELA'.center(tam, "="))
    if alinhar:
        for k, v in dicio.items():
            print(f'{k:.<30}{v}')
    else:
        for k, v in dicio.items():
            print(f'{k}: {v}')
    print('='*tam)


def titulo(msg):
    print('~'* (len(msg) + 4))
    print('  ' + msg)
    print('~'* (len(msg) + 4))
