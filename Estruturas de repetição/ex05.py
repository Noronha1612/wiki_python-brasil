from functions.validação import lerFloat, lerInt

popA = lerInt('Popoulação do país A: ', pos=True, erro='Digite uma população válida')
while True:
    creA = lerFloat('Taxa de crescimento, em %, do país A: ', pos=True, erro='Digite um valor entre 0 e 100')
    if 0 <= creA <= 100:
        break
    print('Digite um valor entre 0 e 100') 

popB = lerInt('População do país B: ', pos=True, erro='Digite uma população válida')
while True:
    creB = lerFloat('Taxa de crescimento, em %, do país B: ', pos=True, erro='Digite um valor entre 0 e 100')
    if 0 <= creB <= 100:
        break
    print('Digite um valor entre 0 e 100')

pais1 = [popA, creA/100, 'país A']
pais2 = [popB, creB/100, 'país B']
iguais = False
if pais1[0] == pais2[0]:
    iguais = True

print('-='*35)
if not iguais:
    if pais1[0] > pais2[0]:
        maior = pais1
        menor = pais2
    else:
        maior = pais2
        menor = pais1
    if menor[1] < maior[1] or menor[0] == 0:
        print(f'A população do {menor[2]} nunca chegará a população do {maior[2]}.')
    else:
        anos = 0
        while menor[0] < maior[0]:
            anos += 1
            menor[0] += menor[0] * menor[1]
            maior[0] += maior[0] * maior[1]
        print(f'São necessários {anos} anos para a população do {menor[2]} ultrapassar a população do {maior[2]}')

else:
    print('A população dos 2 países são inicialmente iguais.')
print('-='*35)
