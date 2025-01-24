""" Solução 1 """

# numeros = [1,2,3,4,5,6,7,8,9,10]
# soma = 0

# for num in numeros:
#     if num % 2 != 0:
#         soma += num
    
# print(soma)

""" Solução 2 """
soma_impares = 0

for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)