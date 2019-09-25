dist = float(input('Informe a distância da viagem em Km: '))
if dist > 200.0:
    print('O custo da viagem é de R${:.2f}'.format(dist*0.45))
else:
    print('O custo da viagem é de R${:.2f}'.format(dist*0.50))
