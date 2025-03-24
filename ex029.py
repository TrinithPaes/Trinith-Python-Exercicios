carro = float(input('Qual é a velocidade atual do carro? '))
multa = (carro - 80) * 7
if carro >= 80:
    print('MULTADO! Você excedeu o limite permitido que 80km/h')
    print('Você deve pagar uma multa de R$:{:.2f}!'.format(multa))
print('Tenha um bom dia! dirija com segurança.')