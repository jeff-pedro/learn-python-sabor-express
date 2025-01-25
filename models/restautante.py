class Restaurante:
    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    

restaurante_guaco = Restaurante('Guaco', 'Fast-Food')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

print(vars(restaurante_guaco))
print(vars(restaurante_pizza))

# print(vars(restaurante_guaco)) # vars -> dicionário com as propriedades do objeto
# print(dir(restaurante_guaco)) # dir -> lista com todos os atributos e métodos do objeto
