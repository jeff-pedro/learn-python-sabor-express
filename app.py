# from models.menu import Menu
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida

bebida_suco = Bebida('Suco de Laranja', 5.0, 'grande')
prato_lasanha = Prato('Lasanha', 30, 'Lasanha duo com molho vemelho e branco')

def main():
    # Menu.exibir_menu()
    print(bebida_suco)
    print(prato_lasanha)

if __name__ == '__main__':
    main()
