from carro import Carro

# Instância 3 objetos da classe Carros
carro1 = Carro(marca='Honda', modelo='Civic', portas=4, cor='prata')
carro2 = Carro(marca='Toyota', modelo='Hilux', portas=4, cor='vermelha')
carro3 = Carro(marca='Chevrolet', modelo='Celta', portas=2, cor='preto')

# Ligando o carro1
print(carro1.ligar())

print(carro1)