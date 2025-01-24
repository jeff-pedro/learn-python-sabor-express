""" Solução 1 """
# import json

# frase = 'Não espere pelo momento perfeito. Faça de cada momento a oportunidade perfeita.'
# palavras = []

# for palavra in frase.replace('.','').split(' '):
#     palavras.append({
#         'palavra': palavra,
#         'ocorrencia': frase.count(palavra)
#     })

# print(json.dumps(palavras, indent=4, ensure_ascii=False))


""" Solução 2 """
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.replace('.', '').split(' ')

for palavra in palavras:
    # contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1  # alternativa
    contagem_palavras[palavra] = frase.count(palavra)

print(contagem_palavras)
