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

    def listar():
        print(f'{"NOME DO RESTAURANTE".ljust(25)} | {"CATEGORIA".ljust(25)} | {"AVALIAÇÃO".ljust(25)} | STATUS')
        print(f'{"-" * 25} | {"-" * 25} | {"-" * 25} | {"-" * 9}')
        

        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.avaliacoes.ljust(25)} | {restaurante.ativo}')
        
        return ''
    
    def cadastrar(restaurantes):
        pass

    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def avaliacoes(self):
        media = 0
        
        for avaliacao in self._avaliacao:
            media += avaliacao._nota / len(self._avaliacao)

        return str(media)


    @property
    def ativo(self):
        return '☒' if self._ativo else '❏'
