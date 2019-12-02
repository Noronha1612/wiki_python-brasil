def lerFloat(msg): #Lê um valor "float" com tratamento de erro
    while True:
        num = input(msg)
        num = num.replace(',', '.')
        v = num.replace('.', '')
        v = v.replace('-', '')
        if v.isnumeric():
            num = float(num)
            if num % 1 == 0:
                num = int(num)
            return num
        print('Digite um valor válido.')
    

def lerInt(msg): #Lê um valor inteiro com tratamento de erro
    while True:
        try:
            num = int(input(msg))
        except:
            print('Digite um valor inteiro válido.')
        else:
            return num


def lerNota(msg): #Lê uma nota de 0 a 10
    while True:
        nota = lerFloat(msg)
        if 0 <= nota <= 10:
            return nota
        print('Digite uma nota válida')


def lerOnlyFloat(msg, erro='Digite um valor flutuante'):
    while True:
        num = lerFloat(msg)
        if str(num).find('.') != -1:
            break
        print(erro)
    return num


def lerSexo(msg):
    while True:
        sexo = input(msg).strip().lower()[0]
        if sexo in 'mf':
            if sexo == 'm':
                return 'masculino'
            else:
                return 'feminino'
        print('Digite M para masculino ou F para feminino.')
