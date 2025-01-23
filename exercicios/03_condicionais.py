usuario_correto = 'jeff'
senha_correta = '123456'

usuario = input('Digite seu usuário: ').strip()
senha = input('Digite sua senha: ').strip()

if usuario == usuario_correto and senha == senha_correta:
    print('Login realizado com sucesso!')
else:
    print('Usuário ou senha incorretos')
