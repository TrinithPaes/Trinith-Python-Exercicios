print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro Termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} → ".format(termo), end="")
    termo += razão
    cont += 1
print("FIM")