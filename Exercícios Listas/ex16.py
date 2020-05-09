from functions.validação import lerFloat, lerInt
from functions.visual import titulo

qtdVend = lerInt("Qual a quantidade de vendedores da empresa: ", erro="Digite uma quantidade válida",pos=True)

contadores = [
    [200, 0, "R$200 e R$299"],
    [300, 0, "R$300 e R$399"],
    [400, 0, "R$400 e R$499"],
    [500, 0, "R$500 e R$599"],
    [600, 0, "R$600 e R$699"],
    [700, 0, "R$700 e R$799"],
    [800, 0, "R$800 e R$899"],
    [900, 0, "R$900 e R$999"],
    [0, "Acima de R$1000"],
]

for x in range (qtdVend):
    valorBruto = lerFloat(f'Valor bruto arrecadado pelo {x + 1}° vendedor: R$', erro="Digite um valor válido", pos=True)

    salario = 200 + valorBruto * 0.09

    for ind, cont in enumerate(contadores):
        if ind != 8:
            if salario >= cont[0] and salario < contadores[ind + 1][0]:
                cont[1] += 1
                break
        else:
            cont[0] += 1

print('\n')
titulo('Registro de salário de vendedores')
print('\n')

for ind, cont in enumerate(contadores):
    if ind != 8:
        if cont[1] != 0:
            if cont[1] == 1:
                print(f'Foi registrado {cont[1]} vendedor com salario entre {cont[2]}')
            else:
                print(f'Foram registrados {cont[1]} vendedores com salario entre {cont[2]}')
    else:
        if cont[0] != 0:
            if cont[0] == 1:
                print(f'Foi registrado {cont[0]} vendedor com salario {cont[1]}')
            else:
                print(f'Foram registrados {cont[0]} vendedores com salario {cont[1]}')
