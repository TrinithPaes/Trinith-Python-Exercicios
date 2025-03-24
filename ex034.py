import math
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    s1 = (salario / 100) * 15 + salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, s1))
if salario > 1250:
    s2 = (salario / 10) + salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, s2))