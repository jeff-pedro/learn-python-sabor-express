class Livro:
    def __init__(self, titulo, autor, paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo_autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'


    def aumentar_paginas(self, quantidade):
        self.paginas = self.paginas + quantidade


class Pessoa:
    def __init__(self, nome, idade, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    def aniversario(self):
        self.idade  +=  1
        return f'Parabéns pelos seus {self.idade} anos {self.nome}!'

    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome} e trabalho como {self.profissao}.'    
        else:
            return f'Olá, sou {self.nome}!'


livro1 = Livro('Kindred', 'Octavia E. Butler', 350)
livro1.aumentar_paginas(50)

# print(livro1)


# Criando 2 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Hermione', idade=30, profissao='Engenheira')
pessoa2 = Pessoa(nome='Dexter', idade=35)

# Imprimindo informações
print('Informações inicias:')
print(pessoa1)
print(pessoa2)
print()

# Método de aniversário para aumentar 1 ano e dar os parabéns
print(pessoa1.aniversario())
print(pessoa2.aniversario())
print()

# Imprimindo informações
print('Informações inicias após anivesário:')
print(pessoa1)
print(pessoa2)
print()

# Método para saudação
print(pessoa1.saudacao())
print(pessoa2.saudacao())
