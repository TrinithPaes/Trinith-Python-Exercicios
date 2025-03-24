real = float(input('Quanto dinheiro voce tem? R$'))
dolar = real / 5.40
euro = real / 5.61
print('Com R${:.2f} você pode comprar US${:.2f} dolares ou EUR${:.2f} euros'.format(real, dolar, euro))
