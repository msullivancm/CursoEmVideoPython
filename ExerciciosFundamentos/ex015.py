distancia = float(input('Quantidade de Km percorridos: Km'))
dias = int(input('Quantidade de dias do aluguel: '))
precoAPagar = (60 * dias) + (distancia * 0.15)
print('Preço total a pagar é de R${:.2f}'.format(precoAPagar))