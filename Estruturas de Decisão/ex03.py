#Esse exemplo pode ser resolvido pela função "lerSexo()" em "validação.py"

sexoinp = input('Digite seu sexo: [M/F] ').strip().lower()[0]
if sexoinp == 'm':
    sexo = 'Masculino'
elif sexoinp == 'f':
    sexo = 'Feminino'
else:
    sexo = 'Indefinido'

print(f'Foi registrado sexo "{sexo}"')
