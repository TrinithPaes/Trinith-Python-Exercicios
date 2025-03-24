soma = 0
cont = 0
for C in range(1, 501, 2):
    if C % 3 == 0:
        soma += C
        cont += 1

print("A soma de todos os {} valores solicitados é {}".format(cont, soma))