from functions.validação import lerInt, lerFloat
from functions.visual import tabela, formatDinheiro
from time import sleep

dados = {}

while True:
    nome = input('Nome: ').strip().lower()
    if len(nome) > 3:
        dados['Nome'] = nome.capitalize()
        break
    print('O nome deve ter mais que 3 caracteres')

while True:
    idade = lerInt('Idade: ')
    if 0 <= idade <= 150:
        dados['Idade'] = idade
        break
    print('Digite uma idade válida.')

while True:
    salario = lerFloat('Salário: R$', erro='Digite um valor')
    if salario > 0:
        dados['Salário'] = formatDinheiro(salario)
        break
    print('Digite uma quantia válida.')

sexos = {
    'f':'Feminino',
    'm':'Masculino'
    }
while True:
    sexo = input('Sexo: [F/M] ').strip().lower()[0]
    if sexo in sexos.keys():
        dados['Sexo'] = sexos[sexo]
        break
    print('Digite um sexo válido')

estados = {
    's':'Solteiro(a)',
    'c':'Casado(a)',
    'd':'Divorciado(a)',
    'v':'Viúvo(a)'
    }
print("""Selecione seu estado civil:
[S] Solteiro(a)
[C] Casado(a)
[D] Divorciado(a)
[V] Viúvo(a)""")

while True:
    ec = input('Sua opção: ').strip().lower()[0]
    if ec in estados.keys():
        dados['Estado Civil'] = estados[ec]
        break
    print('Digite uma opção válida')

print('Guardando dados...')
sleep(1.5)
tabela(dados)
