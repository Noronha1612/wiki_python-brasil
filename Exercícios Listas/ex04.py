from functions.visual import tabela
from time import sleep

letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    texto = input('Digite algo com apenas 10 letras: ').strip()
    if len(texto) == 10:
        valid = True
        for l in texto:
            if l.upper() not in letras:
                valid = False
        if valid:
            break
        print('Caractere(s) inválido(s) encontrado(s). Tente novamente')
    else:
        print('O texto deve conter 10 letras. Tente novamente')

consoantes = []
ncons = 0

for l in texto:
    if l.upper() not in 'AEIOU':
        ncons += 1
        if l not in consoantes:
            consoantes.append(l)



tabela({
    'Número de consoantes encontradas': ncons,
    'Consoantes': '; '.join(consoantes)
}, tam=30)
