# As variáveis poderia ser simplificada assim → n = cont = soma = 0
n = 0
cont = 0
soma = 0
n = int(input("Digite um número [999 para parar]: "))   # Dentro e fora para desconsiderando o flag.

while n != 999:
    soma += n  # soma dos números digitados.
    cont += 1  
    n = int(input("Digite um número [999 para parar]: "))   # Dentro e fora para desconsiderando o flag.

print("Você digitol {} números e a soma entre eles foi {}.".format(cont, soma))
