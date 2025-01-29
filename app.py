# from models.menu import Menu
import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}

    for item in dados_json:

        nome_do_restaurante = item['Company']
        
        if not nome_do_restaurante in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })

        print(dados_restaurante['McDonald’s'])


else:
    print(response.status_code)


def main():
    # Menu.exibir_menu()
    pass

if __name__ == '__main__':
    main()
