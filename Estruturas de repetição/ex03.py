from functions.validação import lerInt
from functions.visual import tabela


def capitalizarNome(nome):
    pos = 0
    letrasnome = []
    for l in nome:
        letrasnome.append(l)
    while True:
        if nome[pos:].find(' ') == -1:
            return ''.join(letrasnome)
        else:
            letrasnome[nome[pos:].find(' ') + 1] = letrasnome[nome[pos:].find(' ') + 1].upper()
        pos = nome[pos:].find(' ') + 1
        



while True:
    nome = capitalizarNome(input('Nome: ').strip().lower().capitalize())
    if len(nome) > 3:
        break
    print('O nome deve ter mais que 3 caracteres')
print(nome)
