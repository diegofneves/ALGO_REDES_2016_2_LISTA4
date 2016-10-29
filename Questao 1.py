senhas = [
    [input('Insira sua senha de 4 digitos: '), input('Insira sua senha de 4 digitos: ')] ,
    [input('Insira sua senha de 4 digitos: '), input('Insira sua senha de 4 digitos: ')]
        ]

for linha in senhas:
    for senha in linha:
        print('Senha cadastrada!')

senha_user = input('Digite sua senha: ')

for linha in senhas:
    for senha_user in linha:
        if senha_user == senha:
            print('Bem vindo!')
        else:
            print('Acesso negado!')