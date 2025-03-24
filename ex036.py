casa = float(input('O valor da casa é: R$'))
salário = float(input('O salário do comprador é: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos aprestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= mínimo:
    print('\33[0;34m')
    print('Empréstimo APROVADO!!!')
else:
    print('\33[031m')
    print('Empréstimo NEGADO!!!')