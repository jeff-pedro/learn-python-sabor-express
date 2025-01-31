from models.restautante import Restaurante

class RestauranteService:
    
    @staticmethod
    def cadastrar_restaurante(nome, categoria):
        restaurante = Restaurante(nome, categoria)
        restaurante.cadastrar()
    
    @staticmethod
    def listar_restaurantes():
        Restaurante.listar()
    
    @staticmethod
    def avaliar_restaurante(nome_restaurante):
        restaurante = Restaurante.buscar_por_nome(nome_restaurante)
        if restaurante:
            try:
                nota = int(input('Digite a nota do restaurante (0 a 5): '))
                if 0 <= nota <= 5:
                    restaurante.receber_avaliacao('Anônimo', nota)
                else:
                    print('\nNota inválida. Dever ser entre 0 e 5.')
                
            except ValueError:
                print('\nNota inválida. Deve ser um número.')
        else:
            print('\nNenhum restaurante encontrado.')

    @staticmethod
    def alternar_status_restaurante(nome_restaurante):
        restaurante = Restaurante.buscar_por_nome(nome_restaurante)
        if restaurante:
            restaurante.alternar_status()
        else:
            print('\nNenhum restaurante encontrado.')

    @staticmethod
    def buscar_restaurante(nome):
        try:
            restaurante = Restaurante.buscar_por_nome(nome)

            if not restaurante:
                raise Exception(f'\nNenhum restaurante chamado {nome.upper()} foi encontrado.')

            return restaurante
        except Exception as e:
            print(e)
