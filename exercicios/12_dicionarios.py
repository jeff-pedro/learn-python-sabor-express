pessoa = { 
    "nome":"Jane", 
    "idade": 35, 
    "cidade": "Cape Town"
}

""" Atualiza Idade """
# pessoa.update({'idade': 30)
pessoa['idade'] = 30

""" Adiciona Profissão """
pessoa['profissao'] = 'Engenheiro'

""" Remove elemento """
# pessoa.pop("cidade")
del pessoa["cidade"]

print(pessoa)

""" Remove elemento """
# del pessoa
