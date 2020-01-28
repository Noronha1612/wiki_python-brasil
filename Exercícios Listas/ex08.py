from functions.validação import lerInt
from functions.visual import tabela

pessoas = []
for x in range(5):
    pessoa = []
    while True:
        idade = lerInt(f'Digite a idade da {x + 1}° pessoa: ', pos=True, erro="Digite uma idade válida")
        if idade < 150:
            break
        print('Digite uma idade válida')
    
    while True:
        altura = lerInt(f'Digite a altura da {x + 1}° pessoa em centímetros: ', erro='Digite uma altura válida')
        if 35 < altura < 280:
            break
        print('Digite uma altura válida')
    i = f'{x+1}°'
    pessoa.append(idade)
    pessoa.append(altura)
    pessoa.append(i)
    pessoas.append(pessoa[:])
    print('Dado registrado com sucesso')
    print()
    print('-='*25)
    print()


dados = {}

for p in pessoas[::-1]:
    dados[f"Idade/Altura da {p[2]} pessoa"] = f"{p[0]}/{p[1]}"

tabela(dados)
