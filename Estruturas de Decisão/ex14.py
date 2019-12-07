from functions.validação import lerNota
from functions.visual import tabela, arredondamento

nota1 = lerNota('Nota 1: ')
nota2 = lerNota('Nota 2: ')
media = (nota1 + nota2) / 2
if media <= 4:
    conceito = 'E'
elif media <= 6:
    conceito = 'D'
elif media <= 7.5:
    conceito = 'C'
elif media <= 9:
    conceito = 'B'
else:
    conceito = 'A'
dados = {
    'Média': arredondamento(media),
    'Conceito': conceito
}

tabela(dados, tam=10)
