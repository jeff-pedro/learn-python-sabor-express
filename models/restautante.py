class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
    
    def cadastrar(restaurantes):
        pass

    def alterar_status():
        pass
    

restaurante_guaco = Restaurante('Guaco', 'Fast-Food')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

print(Restaurante.listar())

# print(restaurante_guaco.listar())
# print(restaurante_pizza)

# print(vars(restaurante_guaco)) # vars -> dicionário com as propriedades do objeto
# print(dir(restaurante_guaco)) # dir -> lista com todos os atributos e métodos do objeto
