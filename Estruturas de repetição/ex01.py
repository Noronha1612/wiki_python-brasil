# Esse programa poderia ser facilmente com a função lerNota() em functions.validacao
while True:
    try:
        nota = float(input('Nota de 0 a 10: '))
    except:
        print('Digite um valor válido')
    else:
        if 0 <= nota <= 10:
            break
        print('Digite uma nota de 0 a 10 válida.')

print('Nota armazenada com sucesso!')
