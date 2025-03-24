n= int(input('Digite um numero: '))
d= n * 2
t= n * 3
r= n ** (1/2)
print('O dobro de {} vale \033[31m{}\033[m '.format(n, d))
print('O tripo de {} vale \033[32m{}\033[m '.format(n, t))
print('A raiz quadrada de {} é Igual a \033[33m{:.2f}\033[m '.format(n, r))
