from models.avaliacao import Avaliacao
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

class Restaurante:
    """ Representa um restaurantes e suas caracteristicas. """

    restaurantes = []

    def __init__(self, nome, categoria, ativo = False):
        """
        Inicia um instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante
        - categoria (str): A categoria do restaurante
        """
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = ativo
        self._avaliacao = []
        self._cardapio = []



    def __str__(self):
        """ Retorna uma representação em string do restaurante. """
        return f'{self._nome} | {self._categoria}'


    @classmethod
    def listar(cls):
        """ Exibe uma lista formatada de todos os restaurantes. """
        print(f'{"NOME DO RESTAURANTE".ljust(20)} | {"CATEGORIA".ljust(20)} | {"AVALIAÇÃO".ljust(20)} | STATUS')
        print(f'{"-" * 20} | {"-" * 20} | {"-" * 20} | {"-" * 9}')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')
        return ''
    
    def listar_cardapio(self):
        print(f'{"NOME".ljust(20)} | {"PREÇO".ljust(20)}')
        print(f'{"-" * 20} | {"-" * 20}')

        for cardapio in self._cardapio:
            print(f'{cardapio._nome.ljust(20)} | {str(cardapio._preco).ljust(20)} ')
        return ''

    def alternar_status(self):
        """ Altera o estado de atividade do restaurante """
        self._ativo = not self._ativo
        print(f'\nRestaurante {self._nome} foi { 'ATIVADO' if self._ativo else 'DESATIVADO' } com sucesso!')
    

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação
        - nota (float): A nota atribuída ao restaurante (entre 0 e 5)
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)


    @property # para deixar o método disponível para ser lido como propriedade do objeto 
    def media_avaliacoes(self):
        """ Calcula e retorna a média das avaliações do restaurante. """
        if not self._avaliacao:
            return '-'

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        
        return media


    @property
    def ativo(self):
        """ Retorna um simbolo indicando o estado de atividade do restaurante. """
        return '☒' if self._ativo else '❏'
    

    def cadastrar(self):
        ''' 
        Essa função é responsável por cadastrar um novo restaurante

        Inputs:
            Objeto Restaurante

        Output: 
            Adiciona um novo restaurante a lista de restaurantes
        '''
        Restaurante.restaurantes.append(self)
        print(f'\nRestaurante {self._nome} foi cadastrado com sucesso!')


    @classmethod
    def buscar_por_nome(cls, nome):
        '''
        Busca restaurante na lista de restaurantes

        Inputs:
            nome (str): nome do restaurante a ser buscado na lista

        Outputs:
            objeto: objeto que representa um restaurante   
        '''
        if not cls.restaurantes:
            return False

        for restaurante in cls.restaurantes:
            if restaurante._nome.upper() == nome:
                return restaurante


    def adicionar_bebida_no_cardapio(self, bebida):
        self._cardapio.append(bebida)


    def adicionar_prato_no_cardapio(self, prato):
        self._cardapio.append(prato)


    # def adicionar_bebida_no_cardapio(self, nome, preco, tamanho):
    #     bebida = Bebida(nome, preco, tamanho)
    #     self._cardapio.append(bebida)
    #     print(f'{nome} adicionado(a) com sucesso\n')


    # def adicionar_prato_no_cardapio(self, nome, preco, descricao):
    #     prato = Prato(nome, preco, descricao)
    #     self._cardapio.append(prato)
    #     print(f'{nome} adicionado(a) com sucesso\n')
