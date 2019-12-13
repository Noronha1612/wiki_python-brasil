from functions.visual import titulo


def escolha(msg):
    while True:
        res = input(msg).upper().strip()[0]
        if res in 'SN':
            return res
        print('Digite uma opção válida.')

titulo('Interrogatório')

print('Apenas digite [S] para positivo e [N] para negativo')
perguntas = [
    'Telefonou para a vítima? ',
    'Esteve no local do crime? ',
    'Mora perto da vítima? ',
    'Devia para a vítima? ',
    'Já trabalhou com a vítima? '
]
contador = 0
for x in range(5):
    perg = escolha(f'Pergunta {x + 1}: ' + perguntas[x])
    if perg == 'S':
        contador += 1

if contador < 2:
    estado = 'INOCENTE'
elif contador < 3:
    estado = 'SUSPEITO(A)'
elif contador < 5:
    estado = 'CÚMPLICE'
else:
    estado = 'ASSASSINO(A)'
    
print('-='*20)
print(f'O interrogado foi classificado como {estado}')
print('-='*20)
