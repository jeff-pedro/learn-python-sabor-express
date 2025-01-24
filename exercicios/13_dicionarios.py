import json

""" Solução 1 """
# numeros_quadrados = []

# for i in range(1, 6):
#     numeros_quadrados.append({
#         'numero': i,
#         'quadrado':  i ** 2
#     })

# print(json.dumps(numeros_quadrados, indent=4))


""" Solução 2 """
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)
