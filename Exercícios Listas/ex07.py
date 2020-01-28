from functions.validação import lerInt
from functions.visual import tabela

nums = []
for x in range(5):
    nums.append(lerInt(f'Digite o {x + 1}° número inteiro: ', erro="\33[1;31mNÚMERO INTEIRO!\33[m"))

mult = 1
soma = 0
for i, n in enumerate(nums):
    mult *= n
    soma += n
    nums[i] = str(nums[i])

tabela({
    'Soma dos números digitados': soma,
    'Multiplicação dos números digitados': mult,
    'Números digitados': '; '.join(nums)
}, tam=42)
