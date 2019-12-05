from functions.validação import lerFloat

num1 = lerFloat('Digite um número: ')
maior = menor = num1
num2 = lerFloat('Digite outro número: ')
if num2 > maior:
    maior = num2
if num2 < menor:
    menor = num2
num3 = lerFloat('Digte o último número: ')
if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

print(f"""Dos valores digitados:
Maior valor: {maior}
Menor valor: {menor}""")
