from functions.validação import lerInt
from datetime import date

ano = lerInt('Digite um ano: ', erro='Digite um ano válido.')
anoatual = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    if ano == anoatual:
        print('O ano atual é bissexto')
    else:
        print(f'O ano {ano} é bissexto')
else:
    if ano == anoatual:
        print('O ano atual não é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')
