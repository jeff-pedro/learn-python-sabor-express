# from models.menu import Menu
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida
from models.cardapio.sobremesa import Sobremesa
from models.restautante import Restaurante

# restaurante_guaco.adicionar_prato_no_cardapio('Burrito', 30, 'Burrito reacheado com barbacoa, queijo e guaca-mole.')
# restaurante_guaco.adicionar_bebida_no_cardapio('Suco de Laranja', 8, 'grande')

bebida_suco = Bebida('Suco de Laranja', 5.0, 'grande')
prato_lasanha = Prato('Lasanha', 30.0, 'Lasanha duo com molho vemelho e branco.')
sobremesa_pudim = Sobremesa('Pudim de Leite', 15, 'doce', 'médio', 'Pudim de leite condensado cremoso com calda de caramelo.')

bebida_suco.aplicar_desconto()
prato_lasanha.aplicar_desconto()

restaurante_guaco = Restaurante('Guaco', 'mexicano')

restaurante_guaco.adicionar_no_cardapio(bebida_suco)
restaurante_guaco.adicionar_no_cardapio(prato_lasanha)
restaurante_guaco.adicionar_no_cardapio(sobremesa_pudim)

def main():
    # Menu.exibir_menu()
    restaurante_guaco.exibir_cardapio

if __name__ == '__main__':
    main()
