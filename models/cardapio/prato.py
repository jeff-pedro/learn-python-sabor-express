from models.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    """ Represensa o item prato do cardápio """
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    
    def __str__(self):
        return super().__str__()
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.05