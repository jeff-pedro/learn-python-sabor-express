class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, ativo = False):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = ativo
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    def listar():
        print(f'{"NOME DO RESTAURANTE".ljust(25)} | {"CATEGORIA".ljust(25)} | STATUS')
        print(f'{"-" * 25} | {"-" * 25} | {"-" * 9}')
        
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
        
        return ''
    
    def cadastrar(restaurantes):
        pass

    def alterar_status(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return '☒' if self._ativo else '❏'


restaurante_guaco = Restaurante('guaco', 'fast-food')
restaurante_pizza = Restaurante('pizza express', 'italiana')

print(restaurante_guaco.alterar_status())

print(Restaurante.listar())

# vars() -> mostra dicionário com as propriedades do objeto/classe
# dir() -> mostra lista com todos os atributos e métodos do objeto/classe
