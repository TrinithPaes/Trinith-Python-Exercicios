# Variáveis
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmelher20 = 0

# Loop para coletar os dados de 4 pessoas
for p in range(1, 5):
    print("----- {}° PESSOA -----".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade

    # Se for o primeiro homem analisado, ele é automaticamente o mais velho até o momento
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome

    # Verifica se a pessoa é um homem e se tem idade maior que a registrada como a maior até o momento
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    # Verifica se a pessoa é uma mulher e tem menos de 20 anos
    if sexo in "Ff" and idade < 20:
        totmelher20 += 1

# Calcula a média de idade do grupo
mediaidade = somaidade / 4

# Exibe os resultados finais
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totmelher20))