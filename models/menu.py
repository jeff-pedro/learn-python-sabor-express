import os
from models.restautante import Restaurante

class Menu:
    ''' Representa o menu principal '''
    restaurantes = []

    @classmethod
    def exibir(cls):
        cls.limpar_tela()
        cls.exibir_nome()
        cls.exibir_opcoes()
        cls.escolher_opcoes()

    @staticmethod
    def limpar_tela():
        os.system('clear')

    @staticmethod
    def exibir_nome():
        ''' Imprime o nome estilizado do programa no terminal ''' 
        print('*' * 70)
        print('''
            █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
            ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
        ''')
        print('*' * 70)
        print()

    @staticmethod
    def exibir_opcoes():
        ''' Exibe as opções de funcionalidades do aplicativo no menu principal '''
        opcoes = [
            '1. Cadastrar restaurante',
            '2. Listar restaurante',
            '3. Avaliar restaurante',
            '4. Ativar | Desativar restaurante',
            '5. Sair\n'
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
                5: cls.finalizar_app
            }
            opcoes.get(opcao_escolhida, cls.opcao_invalida)()
        except ValueError:
            cls.opcao_invalida()
        
    @classmethod
    def cadastrar_restaurante(cls):
        cls.limpar_tela()
        cls.exibir_subtitulos('Cadastro de novos restaurantes')
        nome = cls.obter_input_valido('Nome')
        categoria = cls.obter_input_valido('Categoria')
        restaurante = Restaurante(nome, categoria)
        restaurante.cadastrar()
        cls.voltar_ao_menu_principal()

    @classmethod
    def listar_restaurante(cls):
        cls.limpar_tela()
        cls.exibir_subtitulos('Lista de restaurantes')
        Restaurante.listar()
        cls.voltar_ao_menu_principal()

    @classmethod
    def avaliar_restaurante(cls):
        cls.limpar_tela()
        cls.exibir_subtitulos('Avaliando o restaurante')
        nome_restaurante = input('Digite o nome do restaurante: ').strip().upper()
        restaurante = Restaurante.buscar_por_nome(nome_restaurante)

        if restaurante:
            try:
                nota = int(input('Digite a nota do restaurante (0 a 5): '))
                if 0 <= nota <= 5:
                    restaurante.receber_avaliacao('Anônimo', nota)
                else:
                    print('\nNota inválida. Dever ser entre 0 e 5.')
                
            except ValueError:
                print('\nNota inválida. Deve ser um número.')
        else:
            print('\nNenhum restaurante encontrado.')

        cls.voltar_ao_menu_principal()

    @classmethod
    def alternar_status_restaurante(cls):
        cls.limpar_tela()
        cls.exibir_subtitulos('Alternando o estado do restaurante')
        nome_restaurante = input('Digite o nome do restaurante: ').strip().upper()
        
        restaurante = Restaurante.buscar_por_nome(nome_restaurante)
        if restaurante:
            restaurante.alternar_status()
        else:
            print('\nNenhum restaurante encontrado.') 
        
        cls.voltar_ao_menu_principal()

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
    
    @staticmethod
    def exibir_subtitulos(texto):
        ''' 
        Exibe um titulo estilizado no terminal

        Inputs:
            texto (str): texto do subtítulo
        '''
        Menu.limpar_tela
        linha = '*' * len(texto)
        print(linha)
        print(texto.upper())
        print(linha)
        print()

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
