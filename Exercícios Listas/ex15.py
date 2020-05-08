from functions.validação import media
from functions.visual import arredondamento, titulo

notas = []

counter = 0

while True:
    counter += 1

    while True:
        error = "Digite uma nota válida"
        try:
            valor = input(f'Digite a {counter} nota: (Digite "-1" para parar) ')

            valor = valor.replace(',', '.')

            valor = float(valor)

            if valor % 1 == 0:
                valor = int(valor)

            if 0 <= valor <= 10 or valor == -1:
                break
            
            print(error)
        except:
            print(error)

    if valor == -1:
        break

    notas.append(valor)

print(f'\n\nQuantidade de notas informadas: {len(notas)}\n')

print(f'Notas no sentido em que foram informadas: ', end="")
for nota in notas:
    print(nota, end="; ")
print('\n')

notas.reverse()
notasSenInv = notas[:]
notas.reverse()

print(f'Notas no sentido inverso em que foram informadas:')
for nota in notasSenInv:
    print(nota)
print()

print(f'Soma das notas: {arredondamento(sum(notas))}\n')

print(f'Média das notas: {arredondamento(media(notas))}\n')

qtdNotasAcima = 0

for nota in notas:
    if nota > media(notas):
        qtdNotasAcima += 1

print(f'Quantidade de notas acima da media: {qtdNotasAcima}\n')

qtdNotasAbaixo7 = 0

for nota in notas:
    if nota < 7:
        qtdNotasAbaixo7 += 1

print(f'Quantidade de notas abaixo de 7: {qtdNotasAbaixo7}\n')

titulo('Programa encerrado')
