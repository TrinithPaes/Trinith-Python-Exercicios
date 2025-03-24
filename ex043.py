# CALCULADORA DE IMC

peso = float(input("Qual é o seu peso? (kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)
print("O seu IMC é de {:.1f}".format(imc))
if imc <18.5:
    print("\033[0;34m Você está ABAIXO DO PESO!\033[m")
elif imc >=18.5 and imc <25:
    print("\033[0;32m PARABÉNS Você está com o peso IDEAL!\033[m")
elif imc >=25 and imc <30:
    print("\033[0;33m Você está com SOBREPESO!\033[m")
elif imc >=30 and imc <40:
    print("\033[0;35m Você está com OBESIDADE\033[m")
elif imc >=40:
    print("\033[0;31m CUIDADO! Você está com OBESIDADE MÓRBIDA\033[m")

#Colocando Cores no seu programa em Python.
#Teste ----> "\033[mTeste\033[m (padrão do terminal)
