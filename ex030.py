numero = int(input('Digite um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O múnero {} é PAR!'.format(numero))
else:
    print('O número {} é ÍMPAR!'.format(numero))