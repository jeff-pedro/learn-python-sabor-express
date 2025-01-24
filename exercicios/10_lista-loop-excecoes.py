# numeros = [1,2,3,4,5,6,7,8,9,'10'] # para dar erro
numeros = [1,2,3,4,5,6,7,8,9,10]
soma = 0

try:
    for num in numeros:
        soma += num
    print(f'Soma dos elementos: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
