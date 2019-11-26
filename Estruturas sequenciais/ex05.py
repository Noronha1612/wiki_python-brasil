from functions.validação import lerFloat
print("""\33[1;33mSelecione uma opção: 
[1] Metros -> Centímetros
[2] Centímetros -> Metros\33[m""") #Opções
while True:
    esc = input('\33[1;34mSua opção: \33[m') #Escolha com tratamento de erro
    if esc == '1' or esc == '2':
        break
    print('Selicione uma opção válida.')
tam = lerFloat('Digite o tamanho: ')
if esc == '1': #Condicional composta para conversão de tamanho
    print(f'O valor de {tam}m em centímetros vale {tam * 100}cm')
else:
    print(f'O valor de {tam}cm em metros vale {tam / 100}m')
