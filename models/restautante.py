class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self._ativo = ativo
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar():
        print(f'{"NOME DO RESTAURANTE".ljust(25)} | {"CATEGORIA".ljust(25)} | STATUS')
        print(f'{"-" * 25} | {"-" * 25} | {"-" * 9}')
        
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
        
        return ''
    
    def cadastrar(restaurantes):
        pass

    def alterar_status(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return '☒' if self._ativo else '❏'
    

restaurante_guaco = Restaurante('Guaco', 'Fast-Food')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

print(restaurante_guaco.alterar_status())

print(Restaurante.listar())

# vars() -> mostra dicionário com as propriedades do objeto/classe
# dir() -> mostra lista com todos os atributos e métodos do objeto/classe
