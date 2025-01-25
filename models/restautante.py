class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_guaco = Restaurante()
restaurante_guaco.nome = 'Guaco'
restaurante_guaco.categoria = 'fast-food'

print(vars(restaurante_guaco)) # vars -> dicionário com as propriedades do objeto
print(dir(restaurante_guaco)) # dir -> lista com todos os atributos e métodos do objeto