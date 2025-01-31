from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self._portas = int(portas)
        self._cor = cor

    def  __str__(self):
        return f'{super().__str__()} - Portas: {self._portas} - Cor: {self._cor}'

    def ligar(self):
        self._ligado = True
        return f'O carro {self._modelo} está ligado.'