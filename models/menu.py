import os
from models.restautante import Restaurante

class Menu:
    """ Representa o menu principal """
    restaurantes = []

    @classmethod
    def exibir_menu(cls):
        os.system('clear')
        cls.exibir_nome()
        cls.exibir_opcoes()
        cls.escolher_opcoes()

    def exibir_nome():
        ''' Imprime o nome estilizado do programa no terminal ''' 
        print('*' * 70)
        print('''
            █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
            ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
        ''')
        print('*' * 70)
        print()


    def exibir_opcoes():
        ''' Exibe as opções de funcionalidades do aplicativo no menu principal '''
        print('1. Cadastrar restaurante')
        print('2. Listar restaurante')
        print('3. Ativar | Desativar restaurante')
        print('4. Sair\n')


    @classmethod
    def escolher_opcoes(cls):
        '''
        Solicita e executa a opção escolhida pelo usuário

        Outputs:
            Executa a opção escolhida pelo usuário 
        '''
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            match opcao_escolhida:
                case 1: 
                    cls.exibir_subtitulos('Cadastro de novos restaurantes')
                    nome = cls.obter_input_valido('Nome')
                    categoria = cls.obter_input_valido('Categoria')
                    restaurante = Restaurante(nome, categoria)
                    Restaurante.cadastrar(restaurante)
                    cls.voltar_ao_menu_principal()
                case 2: 
                    # listar_restaurantes()
                    pass
                case 3: 
                    # alternar_estado_restaurante()
                    pass
                case 4: 
                    cls.finalizar_app()
                    pass
                case _:
                    cls.opcao_invalida()
        except:
            cls.opcao_invalida()
        

    @classmethod
    def opcao_invalida(cls):
        ''' Exibe mensagem de opção inválida e retorna ao menu principal ''' 
        print('\nOpção inválida!')
        print()
        cls.voltar_ao_menu_principal()

    
    @classmethod
    def voltar_ao_menu_principal(cls):
        '''
        Solicita uma tecla para voltar ao menu principal

        Outputs:
            Retorn ao menu principal
        '''
        input('\nPressione ENTER para voltar ao menu principal ')

        cls.exibir_menu()

    
    def finalizar_app():
        ''' Exibe mensagem de finalização do aplicativo '''
        os.system('clear');
        print('Finalizando o app...\n')
        
    
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

    @property
    def id(cls):
        '''
        Gera um identificador único para cada restaurante

        Outputs:
            int: um número inteiro único e sequencial 
        '''
        return 1 if not cls.restaurantes else (cls.restaurantes[-1]['id'] + 1)
    

    @classmethod
    def obter_input_valido(cls, campo):
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
