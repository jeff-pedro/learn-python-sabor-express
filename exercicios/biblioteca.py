from livro import Livro

# Cria e imprime instâncias da classe Livro
livro1 = Livro('Senhor dos Anés - As Duas Torres', 'J.R.R Tolkien', 1954)
livro2 = Livro('Harry Potter e a Pedra Filosofal', 'J.K Rowling', 1997)

print(livro1)
print(livro2)
print()

# Empresta um livro deixando-o indisponível
print(f'Antes de Emprestar: Livro {livro1._titulo} está disponível? {livro1._disponivel}')
livro1.emprestar()
print(f'Depois de Emprestar: Livro {livro1._titulo} está disponível? {livro1._disponivel}')
print()

# Busca Livro por Ano de Publicação
ano_especifico = 1997
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f'Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}')

# print('Livros disponíveis:')
# for livro in livros_por_ano:
#     print(f'- {livro}') 


