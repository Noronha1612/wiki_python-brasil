def arredondamento(num):
    res = num
    if len(str(res)[str(res).find('.'):]) >= 5:
        res = round(res, len(str(res)[str(res).find('.'):str(res).find('000000')]) - 1)
    if res % 1 == 0:
        res = int(res)
    elif res % 0.1 == 0:
        res = round(res, 1)
    return res


def formatDinheiro(num):
    res = f'R${num:.2f}'
    res = res.replace('.',',')
    return res
