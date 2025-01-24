#!/usr/bin/python3.12

import os

restaurantes = []

def exibir_nome_do_programa():
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
''')


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar | Desativar restaurante')
    print('4. Sair\n')


def exibir_subtitulos(texto):
    os.system('clear')

    linha = '*' * len(texto)
    print(linha)
    print(texto.upper())
    print(linha)
    print()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1: 
                cadastrar_restaurante()
            case 2: 
                listar_restaurantes()
            case 3: 
                alternar_estado_restaurante()
            case 4: 
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()


def opcao_invalida():
    print('\nOpção inválida!')
    voltar_ao_menu_principal()


def finalizar_app():
    os.system('clear');
    print('Finalizando o app...\n')


def gerarId():
    return 1 if not restaurantes else (restaurantes[-1]['id'] + 1)


def obter_input_valido(campo):
    valor = input(f'{campo}: ').strip().upper()
    while not valor:
        print(f'{campo} do restaurante não pode ser vazio.')
        valor = input(f'{campo}: ').strip().upper()
    return valor


def cadastrar_restaurante():
    exibir_subtitulos('Cadastro de novos restaurantes')

    nome = obter_input_valido('Nome')
    categoria = obter_input_valido('Categoria')

    # dicionário [{},{}] 
    restaurante = {
        'id': gerarId(),
        'nome': nome,
        'categoria': categoria,
        'ativo': False
    }
    
    restaurantes.append(restaurante)

    print(f'\nRestaurante {nome} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulos('Lista de restaurantes')
    
    try:
        if not restaurantes:
            raise Exception('Nenhum restaurante encontrado.')
    
        nome_tituto = 'NOME DO RESTAURANTE'.ljust(20)
        categoria_titulo = 'CATEGORIA'.ljust(20)
        status_titulo = 'STATUS'

        print(f'{nome_tituto}|{categoria_titulo}|{status_titulo}')
        print(f'{"-" * len(nome_tituto)}|{"-" * len(categoria_titulo)}|{"-" * (len(status_titulo) + 4)}')
        
        for restaurante in restaurantes:
            nome = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ATIVADO' if restaurante['ativo'] else 'DESATIVADO'

            print(f'{nome.ljust(20)}|{categoria.ljust(20)}|{ativo}')

    except Exception as e:
        print(e)

    voltar_ao_menu_principal()


def buscar_restaurante(nome):
    if not restaurantes:
        return False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            return restaurante


def alternar_estado_restaurante():
    exibir_subtitulos('Alternando o estado do restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante: ').strip()
    
    restaurante = buscar_restaurante(nome_restaurante)

    if restaurante:
        restaurante['ativo'] = not restaurante['ativo']
        mensagem = f'\nRestaurante {nome_restaurante} foi { 'ativado' if restaurante['ativo'] else 'desativado' } com sucesso!'
        print(mensagem)
    else:
        print(f'\nNenhum restaurante encontrado!')

    voltar_ao_menu_principal()


def main(): 
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()    
    escolher_opcoes()


if __name__ == '__main__':
    main()
