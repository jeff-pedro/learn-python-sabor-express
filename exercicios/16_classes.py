
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()

# alterando valor de atributo
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

# acessando valor de atributo
nome_do_restaurante = restaurante_praca.nome
print(nome_do_restaurante)

# verificando status
print('Restaurante está ativo!' if restaurante_praca.ativo else 'Restaurante está inativo!')

# armezenando valor do atriburo direto da classe
categoria = Restaurante.categoria

# trocando o valor do atributo
restaurante_praca.nome = 'Bristô'

# criando nova instância
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast-Food'

# verificando valor de atributo
print(f'Categoria é Fast-Food? { 'Fast-Food' in restaurante_pizza.categoria }')

restaurante_pizza.ativo = True

print(f'Nome: {restaurante_pizza.nome}, Categoria: {restaurante_pizza.categoria}')
