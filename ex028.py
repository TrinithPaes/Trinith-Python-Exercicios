from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador pensar
print('-=-'*20)
print('Vou pensar em um nome de 0 á 5 tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em qual numero eu pensei? ')) #Jogador tententa adivinha
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me fencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}!'.format(computador, jogador))


