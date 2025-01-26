from models.restautante import Restaurante

restaurante_guaco = Restaurante('guaco', 'mexicana')

# Avaliações
# restaurante_guaco.receber_avaliacao('Jack', 5)
# restaurante_guaco.receber_avaliacao('Mirian', 4.5)
# restaurante_guaco.receber_avaliacao('Emy', 4)

# print(restaurante_guaco._avaliacao)
print(Restaurante.listar())

def main():
    pass

if __name__ == '__main__':
    main()

# vars() -> mostra dicionário com as propriedades do objeto/classe
# dir() -> mostra lista com todos os atributos e métodos do objeto/classe
