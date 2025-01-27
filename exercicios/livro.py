class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'Titlo: {self._titulo} | Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao}'

    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis
    
    """ Solução 2 """
    # @classmethod
    # def verificar_disponibilidade(cls, ano):
    #     livros_disponiveis = [livro for livro in cls.livros if livro._ano_publicacao == ano and livro._disponivel]
    #     return livros_disponiveis

# obs.: biblioteca.py e main.py importa essa classe