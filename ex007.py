n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
if m < 50 :
    print('\033[31m')
else:
    print('\033[34m')
print("A média entre {:.1f} e {:.1f} é iguam a {:.1f}.".format(n1, n2, m))