from models.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, ativo = False):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = ativo
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar(cls):
        print(f'{"NOME DO RESTAURANTE".ljust(25)} | {"CATEGORIA".ljust(25)} | {"AVALIAÇÃO".ljust(25)} | STATUS')
        print(f'{"-" * 25} | {"-" * 25} | {"-" * 25} | {"-" * 9}')
        

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
        
        return ''
    
    def cadastrar(restaurantes):
        pass

    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property # para deixar o método disponível para ser lido como propriedade do objeto 
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        
        return media

    @property
    def ativo(self):
        return '☒' if self._ativo else '❏'
