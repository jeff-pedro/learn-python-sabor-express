""" Solução 1 """

# lista_de_compras = [
#     {'nome': "Banana", 'quantidade': 12},
#     {'nome': "Maça", 'quantidade': 8},
#     {'nome': "Laranje", 'quantidade': 10}
# ]

# chave = 'nome'

# for elemento in lista_de_compras:
#     if(chave in elemento.keys()):
#         print(f'Chave "{chave}" existe!')
#         break


""" Solução 2 """ 
pessoa = {'nome': 'Amanda', 'idade': 29, 'cidade': 'Recife' }

if 'nome' in pessoa:
    print('A chave "nome" existe no dicionário.')
else:
    print('A chave "nome" NÃO existe no dicionário.')
