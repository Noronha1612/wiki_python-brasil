from functions.validação import lerInt

vezes = lerInt('Quantos termos? ', pos=True, erro='Digite uma quantidade válida')
ant = suc = 1
print('1 1', end=' ')
try:
    for x in range(vezes - 2):
        ter = ant + suc
        print(ter, end=' ')
        ant = suc
        suc = ter
except:
    if vezes == 1:
        print(1)
    elif vezes == 2:
        print('1 1')
    else:
        print('Nenhum número mostrado.')
