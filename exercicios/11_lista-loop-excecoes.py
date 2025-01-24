""" Solução 1 """

# notas = [7,8,9,10]
# somatoria = 0

# try:
#     for nota in notas:
#         somatoria += nota
    
#     media = somatoria / len(notas)
#     print(f'Média das notas: {media}')
# except ZeroDivisionError:
#     print('A lista está vazia. Não é possível calcular a média.')
# except Exception as e:
#     print(f'Ocorreu um erro: {e}')



""" Solução 2 """

notas = [7,8,9,10]
media = 0

try:
    for nota in notas:
        media += nota / len(notas)  
    print(f'Média das notas: {media}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
