print("{:=^40}".format(" LOJAS TRINITH "))
preço = float(input("Preço das compras: R$ "))
print("""FORMA DE PAGAMENTO 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão""")
opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R$:{:.2f}".format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print("Sua compra será parcelada em {}x de R${:.2f} com juros".format(totparc, parcela))
else:
    total = preço
    print("OPÇÃO DE PAGAMENTO INVALIDA, Tente novamente")
print("Sua compra de R$:{:.2f} vai custar R${:.2f} no final." .format(preço, total))
