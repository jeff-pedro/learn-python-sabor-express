import os
from services.restaurante_service import RestauranteService
from utils.display import Display

class Menu:
    ''' Representa o menu principal '''
    restaurantes = []

    @classmethod
    def exibir_menu(cls):
        cls.limpar_tela()
        Display.exibir_nome_programa()
        cls.exibir_opcoes()
        cls.escolher_opcoes()

    @staticmethod
    def limpar_tela():
        os.system('clear')        

    @staticmethod
    def exibir_opcoes():
        ''' Exibe as opções de funcionalidades do aplicativo no menu principal '''
        opcoes = [
            '1. Cadastrar restaurante',
            '2. Listar restaurante',
            '3. Avaliar restaurante',
            '4. Ativar | Desativar restaurante',
            '5. Cadastrar cardápio',
            '6. Listar cardápio',
            '7. Sair\n'
        ]
        print('\n'.join(opcoes))

    @classmethod
    def escolher_opcoes(cls):
        ''' Solicita e executa a opção escolhida pelo usuário '''
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))

            opcoes = {
                1: cls.cadastrar_restaurante,
                2: cls.listar_restaurante,
                3: cls.avaliar_restaurante,
                4: cls.alternar_status_restaurante,
                5: cls.cadastrar_cardapio,
                6: cls.listar_cardapio,
                7: cls.finalizar_app
            }
            opcoes.get(opcao_escolhida, cls.opcao_invalida)()
        except ValueError:
            cls.opcao_invalida()
        
    @classmethod
    def cadastrar_restaurante(cls):
        cls.limpar_tela()
        Display.exibir_subtitulo('Cadastro de novos restaurantes')
        nome = cls.obter_input_valido('Nome')
        categoria = cls.obter_input_valido('Categoria')
        RestauranteService.cadastrar_restaurante(nome, categoria)
        cls.voltar_ao_menu_principal()

    @classmethod
    def listar_restaurante(cls):
        cls.limpar_tela()
        Display.exibir_subtitulo('Lista de restaurantes')
        RestauranteService.listar_restaurantes()
        cls.voltar_ao_menu_principal()

    @classmethod
    def avaliar_restaurante(cls):
        cls.limpar_tela()
        Display.exibir_subtitulo('Avaliando o restaurante')
        nome_restaurante = input('Digite o nome do restaurante: ').strip().upper()
        RestauranteService.avaliar_restaurante(nome_restaurante)
        cls.voltar_ao_menu_principal()

    @classmethod
    def alternar_status_restaurante(cls):
        cls.limpar_tela()        
        Display.exibir_subtitulo('Alternando o estado do restaurante')
        nome_restaurante = input('Digite o nome do restaurante: ').strip().upper()
        RestauranteService.alternar_status_restaurante(nome_restaurante) 
        cls.voltar_ao_menu_principal()

    @classmethod
    def cadastrar_restaurante(cls):
        pass

    @classmethod
    def listar_restaurante(cls):
        pass


    @classmethod
    def opcao_invalida(cls):
        ''' Exibe mensagem de opção inválida e retorna ao menu principal ''' 
        print('\nOpção inválida!')
        cls.voltar_ao_menu_principal()

    @classmethod
    def voltar_ao_menu_principal(cls):
        ''' Solicita uma tecla para voltar ao menu principal '''
        input('\nPressione ENTER para voltar ao menu principal ')
        cls.exibir_menu()

    @staticmethod
    def finalizar_app():
        ''' Exibe mensagem de finalização do aplicativo '''
        Menu.limpar_tela()
        print('Finalizando o app...\n')

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
