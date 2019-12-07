print("""\33[32mEm que turno você estuda? 
[M] Matutino
[V] Vespertino
[N] Noturno""")
esc = input('Sua opção: ').upper()[0]

print('\33[1;33m')
if esc == 'M':
    print('Bom dia!')
elif esc == 'V':
    print('Boa tarde!')
elif esc == 'N':
    print('Boa noite!')
else:
    print('\33[1;31mValor inválido.')
print('\33[m')