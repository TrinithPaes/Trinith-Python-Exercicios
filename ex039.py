from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    alist = nasc + 18
    print('Ainda falta {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(alist))
else idade > 18:
    saldo = idade - 18
    alist = nasc + 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(alist))
