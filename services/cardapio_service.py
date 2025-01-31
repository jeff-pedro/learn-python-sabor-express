from models.cardapio.item_cardapio import ItemCardapio
from models.restautante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.cardapio.sobremesa import Sobremesa

class CardapioService:
    
    @staticmethod
    def adicionar_no_cardapio(nome_do_restaurante, item):
        try:
            restaurante = Restaurante.buscar_por_nome(nome_do_restaurante)

            if not restaurante:
                raise Exception(f'\nErro ao tentar cadastrar o item {item._nome.upper()}. Restaurante {nome_do_restaurante.upper()} não foi encontrado.')

            if isinstance(item, ItemCardapio):
                restaurante._cardapio.append(item)
                print(f'\n{item._nome.upper()} foi cadastrado com sucesso!')
        except Exception as e:
            print(e)

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
    
    @staticmethod
    def listar_cardapio(nome_do_restaurante):
        try:
            restaurante = Restaurante.buscar_por_nome(nome_do_restaurante)

            if not restaurante:
                raise Exception(f'\nNenhum restaurante chamado {nome_do_restaurante.upper()} foi encontrado.')

            print(restaurante.exibir_cardapio)
        except Exception as e:
            print(e)
