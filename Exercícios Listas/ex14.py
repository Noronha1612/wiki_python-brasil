from functions.validação import lerSimNao
from functions.visual import titulo

titulo('Interrogatório')

counter = 0

for x in range(5):
    perguntas = [
        'Telefonou para a vítima? ',
        'Esteve no local do crime? ',
        'Mora perto da vítima? ',
        'Devia para a vítima? ',
        'Já trabalhou com a vítima? '
    ]

    if lerSimNao(perguntas[x]):
        counter += 1

if counter < 2:
    status = 'INOCENTE'
elif counter < 3:
    status = 'SUSPEITA'
elif counter < 5:
    status = 'CÚMPLICE'
else:
    status = 'ASSASSINO'

print(f'\nO interrogado foi classificado como "{status}"')
