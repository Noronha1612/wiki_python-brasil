from functions.validação import lerFloat
from functions.visual import arredondamento

print('-=-=-= Equação de 2° grau =-=-=-')
a = lerFloat('Digite o valor de "A" da equação: ')
if a != 0:
    b = lerFloat('Digite o valor de "B" da equação: ')
    c = lerFloat('Digite o valor de "C" da equação: ')
    delta = b**2 - 4*a*c
    if delta < 0:
        print('A equação não possui raízes.')
    elif delta == 0:
        res1 = -b / (2*a)
        print('A equação só possui 1 raiz: ')
        print(f'x¹ = {arredondamento(res1)}')
    else:
        res1 = arredondamento((-b + delta**(1/2)) / (2*a))
        res2 = arredondamento((-b - delta**(1/2)) / (2*a) )
        print(f"""As raízes da equação são: 
x¹ = {res1}
x² = {res2}""")
else:
    print('Se o valor de "A" for 0, não há uma equação de 2° grau.')
