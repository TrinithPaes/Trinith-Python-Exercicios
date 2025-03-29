from random import randint  # Importa a função randint para gerar números aleatórios

# O computador escolhe um número aleatório entre 0 e 10
computador = randint(0, 10) 

# Mensagem inicial para o jogador
print("Sou seu computador...Acabei de peensar em um número entre 0 e 10.")
print("Será que você consegue adivinha qual é o númeor?")

# Variável para controlar se o jogador acertou
acertou = False 
# Contador de tentativas
palpites = 0

# Loop que continua até o jogador acertar o número
while not acertou:
    jogador = int(input("Qual é o seu palpite? ")) # O jogador insere um palpite
    palpites += 1 # Incrementa o contador de tentativas

    # Verifica se o palpite está correto
    if jogador == computador:
        acertou = True # Sai do loop se acertar
    else:
        # Dá uma dica se o palpite for menor que o número correto
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        # Dá uma dica se o palpite for maior que o número correto
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")

# Mensagem final informando o número de tentativas até o acerto
print("Acertou com {} tentativas. Parabéns!".format(palpites))