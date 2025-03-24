distancia = float(input('Qual a distância da sua viagem? '))
d1 = distancia * 0.50
d2 = distancia * 0.45
print('Voce está prestes a começar uma viagem de {}.km.'.format(distancia))
if distancia <= 200:
    print('E o preço da sua passagem será de R$:{:.2f}'.format(d1))
else:
    print('E o preço da sua passagem será de R$:{:.2f}'.format(d2))