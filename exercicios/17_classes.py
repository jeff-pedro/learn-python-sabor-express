# class Musica:
#     nome = ''
#     artista = ''
#     duracao = int

class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica('Hotel California', 'Eagles', duracao=390)
musica2 = Musica('Stend Up', 'Cythia Erivo', duracao=410)
musica3 = Musica('Os Garotin', 'Zero a Cem', duracao=245)
