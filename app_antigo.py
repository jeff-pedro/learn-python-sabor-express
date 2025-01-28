#!/usr/bin/python3.12

import os

restaurantes = []

def exibir_nome_do_programa():
    ''' Imprime o nome estilizado do programa no terminal ''' 
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
''')


def exibir_opcoes():
    ''' Exibe as opções de funcionalidades do aplicativo no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar | Desativar restaurante')
    print('4. Sair\n')


def exibir_subtitulos(texto):
    ''' 
    Exibe um titulo estilizado no terminal

    Inputs:
        texto (str): texto do subtítulo
    '''
    os.system('clear')

    linha = '*' * len(texto)
    print(linha)
    print(texto.upper())
    print(linha)
    print()


def escolher_opcoes():
    '''
    Solicita e executa a opção escolhida pelo usuário

    Outputs:
        Executa a opção escolhida pelo usuário 
    '''
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
    '''
    Solicita uma tecla para voltar ao menu principal

    Outputs:
        Retorn ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()


def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal ''' 
    print('\nOpção inválida!')
    voltar_ao_menu_principal()


def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    os.system('clear');
    print('Finalizando o app...\n')


def gerarId():
    '''
    Gera um identificador único para cada restaurante

    Outputs:
        int: um número inteiro único e sequencial 
    '''
    return 1 if not restaurantes else (restaurantes[-1]['id'] + 1)


def obter_input_valido(campo):
    ''' 
    Obtem, formata e valida se o valor do input não está vazio

    Inputs:
        campo (str): campo/mensagem que será apresentada no input

    Outputs:
        string:  valor do input formatado e em letras maíusculas 
    '''
    valor = input(f'{campo}: ').strip().upper()
    while not valor:
        print(f'{campo} do restaurante não pode ser vazio.')
        valor = input(f'{campo}: ').strip().upper()
    return valor


def cadastrar_restaurante():
    ''' 
    Essa função é responsável por cadastrar um novo restaurante

    Inputs:
        Nome do restaurante
        Categoria

    Output: 
        Adiciona um novo restaurante a lista de restaurantes
    '''
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
    ''' 
    Lista os restaurantes contidos na lista

    Outputs:
        Exibe a lista de restaurantes no terminal
    ''' 
    exibir_subtitulos('Lista de restaurantes')
    
    try:
        if not restaurantes:
            raise Exception('Nenhum restaurante encontrado.')
    
        NOME_TITULO = 'NOME DO RESTAURANTE'.ljust(20)
        CATEGORIA_TITULO = 'CATEGORIA'.ljust(20)
        STATUS_TITULO = 'STATUS'

        print(f'{NOME_TITULO}|{CATEGORIA_TITULO}|{STATUS_TITULO}')
        print(f'{"-" * len(NOME_TITULO)}|{"-" * len(CATEGORIA_TITULO)}|{"-" * (len(STATUS_TITULO) + 4)}')
        
        for restaurante in restaurantes:
            nome = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ATIVADO' if restaurante['ativo'] else 'DESATIVADO'

            print(f'{nome.ljust(20)}|{categoria.ljust(20)}|{ativo}')
    except Exception as e:
        print(e)

    voltar_ao_menu_principal()

@classmethod
def buscar_restaurante(nome):
    '''
    Busca restaurante na lista de restaurantes

    Inputs:
        nome (str): nome do restaurante a ser buscado na lista

    Outputs:
        string: dicionario encontrado que representa um restaurante   
    '''
    if not restaurantes:
        return False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            return restaurante


def alternar_estado_restaurante():
    ''' 
    Altera o estado ativo/inativo de um restaurante

    Inputs:
        Nome do restaurante

    Outputs:
        Mensagem de sucesso quando a propriedade 'ativo' é alterada para True ou False
    '''
    exibir_subtitulos('Alternando o estado do restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante: ').strip().upper()
    
    restaurante = buscar_restaurante(nome_restaurante)

    if restaurante:
        restaurante['ativo'] = not restaurante['ativo']
        mensagem = f'\nRestaurante {nome_restaurante} foi { 'ativado' if restaurante['ativo'] else 'desativado' } com sucesso!'
        print(mensagem)
    else:
        print(f'\nNenhum restaurante encontrado!')

    voltar_ao_menu_principal()


def main(): 
    ''' Função principal que inicia o programa '''
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()    
    escolher_opcoes()


if __name__ == '__main__':
    main()
