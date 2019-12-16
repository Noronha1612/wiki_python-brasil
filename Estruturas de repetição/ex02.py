while True:
    nome = input('Nome: ').strip()
    senha = input('Senha: ').strip()
    if senha.replace(' ', '').lower() in nome.replace(' ', '').lower():
        print('A senha não pode ser igual ao nome. Tente novamente')
    else:
        print('Senha armazenada com sucesso.')
        break
        