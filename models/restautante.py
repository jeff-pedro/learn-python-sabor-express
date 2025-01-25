class Restaurante:
    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}' 

    

restaurante_guaco = Restaurante('Guaco', 'Fast-Food')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

print(restaurante_guaco)
print(restaurante_pizza)

# print(vars(restaurante_guaco)) # vars -> dicionário com as propriedades do objeto
# print(dir(restaurante_guaco)) # dir -> lista com todos os atributos e métodos do objeto
