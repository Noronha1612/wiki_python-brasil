from functions.validação import media, lerNota

nota1 = lerNota('Nota 1: ')
nota2 = lerNota('Nota 2: ')
media = media(nota1, nota2)

if media < 7:
    estado = 'Reprovado'
elif media < 10:
    estado = 'Aprovado'
else:
    estado = 'Aprovado com distinção'

print('-='*15)
print(f"""Média: {media}
Situação: {estado}""")
print('-='*15)
