dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
nd = dias * 60
nkm = km * 0.15
total = nd + nkm
print('O total apaga é de R${:.2f}'.format(total))
