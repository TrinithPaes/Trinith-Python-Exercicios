from datetime import date
nasc = int(input("Ano de nascimento: "))
ano = date.today().year
idade = ano - nasc
print("O atleta tem {} anos.".format(idade))
if idade <= 9 :
    print("Categoria: MIRIM")
elif idade <= 14 :
    print("Categoria: INFANTIL")
elif idade <=19 :
    print("Categoria: JÚNIO")
elif idade <=25 :
    print("Categoria: SÉNIO")
else:
    print("Categoria: MASTER")