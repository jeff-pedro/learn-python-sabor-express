from models.cardapio.item_cardapio import ItemCardapio
from models.restautante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.cardapio.sobremesa import Sobremesa

class CardapioService:
    
    @staticmethod
    def adicionar_no_cardapio(nome_do_restaurante, item):
        restaurante = Restaurante.buscar_por_nome(nome_do_restaurante)
        if isinstance(item, ItemCardapio):
            restaurante._cardapio.append(item)
            print(f'\n{item._nome} foi cadastrado com sucesso!')

    @staticmethod
    def criar_item_prato(nome, preco, descricao):
        prato = Prato(nome, preco, descricao)
        return prato
    
    @staticmethod
    def criar_item_sobremesa(nome, preco, tipo, tamanho, descricao):
        sobremesa = Sobremesa(nome, preco, tipo, tamanho, descricao)
        return sobremesa

    @staticmethod
    def criar_item_bebida(nome, preco, descricao):
        bebida = Bebida(nome, preco, descricao)
        return bebida


    # @property
    # def exibir_cardapio(self):
    #     """ Exibe uma lista formatada do cardápio de um restaurnte. """
    #     # print(f'Cardapio do restaurante {self._nome}\n')

    #     for i, item in enumerate(self._cardapio, start=1):
    #         preco_string = f'{item._preco:.2f}'
    #         preco_formatado = preco_string.replace('.', ',')

    #         # if hasattr(item, '_tamanho') and hasattr(item, '_tipo'):
    #         #     complemento = f'Tipo: {item._tipo} | Tamanho: {item._tamanho} | Descrição: {item._descricao}'
    #         # elif hasattr(item, '_tamanho'):
    #         #     complemento = f'Tamanho: {item._tamanho}' 
    #         # else:
    #         #     complemento = f'Descrição: {item._descricao}'
            
    #         if isinstance(item, Bebida):
    #             complemento = f'Tamanho: {item._tamanho}' 
    #         elif isinstance(item, Prato):
    #             complemento = f'Descrição: {item._descricao}'
    #         else:
    #              complemento = f'Tipo: {item._tipo} | Tamanho: {item._tamanho} | Descrição: {item._descricao}'

    #         mensagem = f'{i}. Nome: {item._nome} | Preço: R$ {preco_formatado} | {complemento}'
            
    #         print(mensagem)
    #     return ''
