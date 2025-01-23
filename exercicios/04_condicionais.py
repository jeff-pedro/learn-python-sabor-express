x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))

if x > 0 and y > 0:
    print('O ponto está no primeiro Quadrante')
elif x < 0 and y > 0:
    print('O ponto está no segundo Quadrante')
elif x < 0 and y < 0:
    print('O ponto está no terceiro Quadrante')
elif x > 0 and y < 0:
    print('O ponto está no quarto Quadrante')
else:
    print('Eixo localizado no eixo ou origem')
