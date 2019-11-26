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
            num = int(input('Digite um número inteiro: '))
        except:
            print('Digite um valor inteiro válido.')
        else:
            return num

def lerNota(msg):
    while True:
        nota = lerFloat(msg)
        if 0 <= nota <= 10:
            return nota
        print('Digite uma nota válida')
    
