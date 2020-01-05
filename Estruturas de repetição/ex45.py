from functions.visual import tabela, titulo, arredondamento

titulo('Gabarito')

naluno = soma = 0
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
opc = ['A', 'B', 'C', 'D', 'E']
alunos = []
while True:
    naluno += 1
    resp = []
    for x in range(10):
        while True:
            res = input(f'Resposta da {x + 1}° questão: ').upper().strip()
            if res in opc:
                break
            print('Digite uma resposta válida')
        resp.append(res)
    certas = 0
    for i, r in enumerate(gabarito):
        if r == resp[i]:
            certas += 1
    print(f'Sua nota: {certas:.1f}')
    alunos.append([f'Aluno {naluno}', certas])
    while True:
        esc = input('Mais alguém a registrar? [S/N] ').strip().upper()
        if esc == 'S' or esc == 'N':
            break
        print('Selecione apenas "S" para sim e "N" para não')
    if esc == 'N':
        break

maior = [0,0]
menor = [0,0]
for p in alunos:
    if p[0] == 'Aluno 1' or p[1] > maior[1]:
        maior = p
    if p[0] == 'Aluno 1' or p[1] < menor[1]:
        menor = p
    soma += p[1]

media = arredondamento(soma / len(alunos))

dados = {
    'Aluno com mais acertos': f'{maior[0]} com {maior[1]} {"acerto" if maior[1] == 1 else "acertos"}',
    'Aluno com menos acertos': f'{menor[0]} com {menor[1]} {"acerto" if menor[1] == 1 else "acertos"}',
    'Quantidade de alunso registrados': f'{naluno} {"aluno" if naluno == 1 else "alunos"}',
    'Média de notas da turma': media
}

tabela(dados)
