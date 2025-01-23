#!/usr/bin/python3.12

import os
import json

restaurantes = []

def exibir_nome_do_programa():
    print('''
█▀ █▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▄█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
''')


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def exibir_subtitulos(texto):
    os.system('clear')
    print(f'=== {texto} ===\n')


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1: 
                cadastrar_restaurante()
            case 2: 
                listar_restaurantes()
            case 3: 
                ativar_restaurante()
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
    if (len(restaurantes) == 0):
        return 1
    else:
        return restaurantes[-1]['id'] + 1


def cadastrar_restaurante():
    exibir_subtitulos('Cadastro de novos restaurantes')

    nome = input('Nome: ')
    categoria = input('Categoria: ')
    tipo_comida = input('Tipo de comida: ')

    restaurante = {
        'id': gerarId(),
        'nome': nome,
        'categoria': categoria,
        'tipo_comida': tipo_comida,
        'ativo': False
    }
    
    restaurantes.append(restaurante)

    print(f'\nRestaurante {nome} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulos('Lista de restaurantes')
    
    lista_de_restaurantes = json.dumps(restaurantes, indent=4)

    if len(restaurantes) > 0:
        print(lista_de_restaurantes)
        voltar_ao_menu_principal()
    else:
        print('Nenhum restaurante cadastrado!')
        voltar_ao_menu_principal()


def ativar_restaurante():
    exibir_subtitulos('Ativando restaurantes')
    
    id = int(input('Digite o ID do restaurante: '))
    
    for restaurante in restaurantes:
        if (restaurante['id'] == id):
            restaurante['ativo'] = True
    
    print(f'\nRestaurante com id {id} atualizado com sucesso!')
    voltar_ao_menu_principal()


def main(): 
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()    
    escolher_opcoes()


if __name__ == '__main__':
    main()
