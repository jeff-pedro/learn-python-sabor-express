import os

class Display():
    ''' Disponibiliza métodos para exibição de mensagens formatadas de texto. '''

    @staticmethod
    def exibir_nome_programa():
        ''' Imprime o nome estilizado do programa no terminal ''' 
        print('*' * 70)
        print('''
            █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
            ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
        ''')
        print('*' * 70)
        print()

         
    @staticmethod
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

        

