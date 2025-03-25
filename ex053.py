frase = str(input("Digite uma frase: ")).strip().upper() #STRIP eleminar os espaços antes e depois| UPPER coloca tudo em mauscula
palavras = frase.split() #Separei ele em um vetor (uma lista)
junto = "".join(palavras) #Juntei tudo em uma string só.
inverso = ""
for letra in range(len(junto) -1, -1, -1): #Fiz o inverso da frase.
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")