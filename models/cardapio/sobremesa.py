from models.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    """ Represensa o item sobremesa do cardápio """
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def __str__(self):
        return super().__str__()
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.15
    
    