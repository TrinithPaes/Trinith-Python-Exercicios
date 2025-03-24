from random import randint
from time import sleep
from colorama import Fore
# função randint do módulo random -> randint(a, b) gera um número inteiro aleatório entre a e b (inclusive).
# Função sleep do módulo time -> sleep(segundos) pausa a execução do código pelo número de segundos informado.
# Importando a biblioteca colorama para permitir a personalização de cores no terminal.
# O Fore é usado para mudar a cor do texto, enquanto Back altera o fundo e Style define estilos como negrito.

# Definição das opções do jogo
itens = ("Pedra", "Papel", "Tesoura")

# Computador faz sua escolha
computador = randint(0, 2) # Gera um número entre 0 e 2

# Exibe as opções para o jogador
print(""" Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA """)

# Jogador escolhe sua jogada
jogador = int(input("Qual é a sua Jogada? "))

# Contagem regressiva
print("JO")
sleep(1) # Aguarda 1 segundos
print("KEN")
sleep(1)
print("PO!!!")
print("-=" * 11)

# Exibição das escolhas
print("computador jogou {}".format(itens[computador]))
print("Jogador jogou {}" .format(itens[jogador]))
print("-=" * 11)

# Determinação do vencedor
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print(Fore.BLUE + "EMPATE")
    elif jogador == 1:
        print(Fore.GREEN + "JOGADOR VENCEU")
    elif jogador == 2:
        print(Fore.RED + "COMPUTADOR VENCEU")
    else:
        print(Fore.CYAN + "JOGADA INVALIDA")

elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print(Fore.RED + "COMPUTADOR VENCEU")
    elif jogador == 1:
        print(Fore.BLUE + "EMPATE")
    elif jogador == 2:
        print(Fore.GREEN + "JOGADOR VENCEU")
    else:
        print(Fore.CYAN + "JOGADA INVALIDA")

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print(Fore.GREEN + "JOGADOR VENCEU")
    elif jogador == 1:
        print(Fore.RED + "COMPUTADOR VENCEU")
    elif jogador == 2:
        print(Fore.BLUE + "EMPATE")
    else:
        print(Fore.CYAN + "JOGADA INVALIDA")