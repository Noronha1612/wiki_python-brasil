ant = meio = 1
suc = 2
print('0 1 1', end=' ')
while suc < 500:
    suc = meio + ant
    if suc < 500:
        print(suc, end=' ')
    ant = meio
    meio = suc
