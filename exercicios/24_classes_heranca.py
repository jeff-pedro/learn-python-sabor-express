class Banco:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco


class Agencia (Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero