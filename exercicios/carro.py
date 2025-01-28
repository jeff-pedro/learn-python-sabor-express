from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = int(portas)

    def  __str__(self):
        return f'{super().__str__()} - Portas: {self.portas}'
