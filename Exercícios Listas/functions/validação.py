def lerFloat(msg, erro='Digite um valor válido.', pos=False): #Lê um valor "float" com tratamento de erro
    while True:
        num = input(msg)
        num = num.replace(',', '.')
        v = num.replace('.', '')
        v = v.replace('-', '')
        if v.isnumeric():
            num = float(num)
            if num % 1 == 0:
                num = int(num)
            if pos:
                if num >= 0:
                    return num 
            else:
                return num
        print(erro)
    

def lerInt(msg, erro='Digite um valor inteiro válido.', pos=False): #Lê um valor inteiro com tratamento de erro
    while True:
        try:
            num = int(input(msg))
        except:
            print(erro)
        else:
            if pos:
                if num >= 0:
                    return num
                print(erro)
            else: 
                return num


def lerNota(msg, erro='Digite uma nota de 0 a 10 válida'): #Lê uma nota de 0 a 10
    while True:
        nota = lerFloat(msg)
        if 0 <= nota <= 10:
            return nota
        print(erro)


def lerOnlyFloat(msg, erro='Digite um valor flutuante'):
    while True:
        num = lerFloat(msg)
        if str(num).find('.') != -1:
            break
        print(erro)
    return num


def lerSexo(msg, erro='Digite M para masculino ou F para feminino.'):
    while True:
        sexo = input(msg).strip().lower()[0]
        if sexo in 'mf':
            if sexo == 'm':
                return 'masculino'
            else:
                return 'feminino'
        print(erro)


def media(nums): #Para listas
    return sum(nums) / len(nums)


def lerSimNao(msg, erro='Digite apenas "S" para "SIM" ou "N" Para Não'):
    while True:
        opcao = input(msg).strip().lower()[0]
        if opcao == 's':
            return True
        elif opcao == 'n':
            return False
        print(erro)


def lerHoraPorDia(msg, erro='Digite uma hora válida.'):
    while True:
        hora = lerInt(msg, pos=True, erro=erro)
        if hora <= 24:
            return hora
        print(erro)
