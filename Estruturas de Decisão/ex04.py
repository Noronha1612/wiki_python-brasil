while True:
    inp = input('Digite uma letra: ').strip().lower()
    if len(inp) == 1 and inp in 'abcdefghijklmnopqrstuvwxyz':
        break
    if len(inp) != 1:
        print('Digite apenas uma letra')
    else:
        print('Digite uma LETRA')

if inp in 'aeiou':
    condicao = 'vogal'
else:
    condicao = 'consoante'

print(f'A letra digitada foi uma {condicao}')
