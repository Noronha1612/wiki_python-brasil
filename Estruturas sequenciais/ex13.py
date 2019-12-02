from functions.validação import lerFloat, lerSexo
from functions.visual import arredondamento

#Ler altura
while True:
    altura = lerFloat('Digite sua altura em metros: ')
    if 0.5 <= altura <= 3:
        break
    print('Digite uma altura em metros válida.')

#Ler sexo
sexo = lerSexo("""[M] Masculino
[F] Feminino
Seu sexo: """)

#Retornar o peso ideal
if sexo == 'masculino':
    print(f'Seu peso ideal é de {arredondamento(72.7 * altura - 58)}Kg')
else:
    print(f'Seu peso ideal é de {arredondamento(62.1 * altura - 44.7)}Kg')

