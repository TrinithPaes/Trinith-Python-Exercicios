l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
aria = l * a
tinta = aria / 2
print('Sua parede tem a dimensão de {}x{} e sua ária é de {}m².\nPara pintar essa parede, você precisrá de {}l de tinta.'.format(l, a, aria, tinta))
