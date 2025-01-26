from models.restautante import Restaurante

restaurante_guaco = Restaurante('guaco', 'mexicana')
restaurante_lamassa = Restaurante('la massa', 'italiana')
restaurante_nafaca = Restaurante('nafaca', 'american burguer')

restaurante_guaco.alternar_status()

print(Restaurante.listar())

def main():
    pass

if __name__ == '__main__':
    main()