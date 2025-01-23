""" Iterando Com FOR """
""" obs.: usado quando conhecemos préviamente o número de iterações """

# for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
#     numero = int(input("Digite um número positivo: "))
#     if numero > 0:
#         break

# print("Você digitou:", numero)


""" Iterando com WHILE """
numero = -1
while numero < 0: # condição
    numero = int(input("Digite um número positivo: ")) # bloco de código a ser repetido


print("Você digitou:", numero)
