from models.menu import Menu



def main():
    ''' Função principal '''
    Menu.exibir_menu()

if __name__ == '__main__':
    main()


# import requests
# import json

# url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
# response = requests.get(url)

# if response.status_code == 200: # verifica o status code
#     dados_json = response.json() # processa os dados
#     dados_restaurante = {}

#     # organiza as informações
#     for item in dados_json:

#         nome_do_restaurante = item['Company']
        
#         if not nome_do_restaurante in dados_restaurante:
#             dados_restaurante[nome_do_restaurante] = []

#         dados_restaurante[nome_do_restaurante].append({
#             'item': item['Item'],
#             'price': item['price'],
#             'description': item['description']
#         })

#     # salva os dados em arquivos
#     for nome_do_restaurante, dados in dados_restaurante.items():
#         nome_do_arquivo = (
#             f'db/{nome_do_restaurante}.json'
#                 .replace(' ', '')
#                 .replace('’', '')
#                 .lower()
#         )
#         with open(nome_do_arquivo, 'w') as arquivo_restaurante:
#             json.dump(dados, arquivo_restaurante, indent=4)

# else:
#     print(f'O erro foi {response.status_code}')
