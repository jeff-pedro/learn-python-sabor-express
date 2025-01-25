class Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliacao, localizacao='', ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.localizacao = localizacao
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

# instânciando um restaurante e atribuindo os valores obrigatórios no construtor
restaurante1 = Restaurante('Massaroca','Gourmet', 100, 4.5)

print(restaurante1)