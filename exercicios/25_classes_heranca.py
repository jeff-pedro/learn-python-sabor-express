from carro import Carro
from moto import Moto

# Cria instâncias das classes Carro e Moto
moto1 = Moto('Honda', 'NXR 160 Bros', 'esportiva')
carro1 = Carro('Toyota', 'Hilux SW4', 4)

# Cria objetos para Carro e Moto
print(moto1)
print(carro1)
print()

# Liga o carro
carro1.ligar()
print(carro1)