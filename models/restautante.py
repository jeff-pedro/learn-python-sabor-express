from models.avaliacao import Avaliacao

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
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """ Retorna uma representação em string do restaurante. """
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar(cls):
        """ Exibe uma lista formatada de todos os restaurantes. """
        print(f'{"NOME DO RESTAURANTE".ljust(25)} | {"CATEGORIA".ljust(25)} | {"AVALIAÇÃO".ljust(25)} | STATUS')
        print(f'{"-" * 25} | {"-" * 25} | {"-" * 25} | {"-" * 9}')
        

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
        return ''
    
    def alternar_status(self):
        """ Altera o estado de atividade do restaurante """
        self._ativo = not self._ativo

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
