import os

class Display:
    ''' Disponibiliza métodos para exibição de mensagens formatadas de texto. '''
    linha = '*' * 78
    
    @staticmethod
    def exibir_nome_programa():
        ''' Imprime o nome estilizado do programa no terminal ''' 
        
        print(Display.linha)
        print('''
                █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
                ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
        ''')
        print(Display.linha)
        print()

         
    @staticmethod
    def exibir_subtitulo(texto):
        ''' 
        Exibe um titulo estilizado no terminal

        Inputs:
            texto (str): texto do subtítulo
        '''
        os.system('clear')        
        # linha = '*' * len(texto)

        centralizado = int(len(Display.linha))
        print(Display.linha)
        print(texto.upper().center(centralizado))
        print(Display.linha)
        print()



