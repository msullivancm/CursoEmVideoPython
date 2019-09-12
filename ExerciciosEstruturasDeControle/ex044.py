preco = float(input('Qual é o preço do produto: R$'))
condPag = int(input('Qual é a condição de pagamento? \n1 -A vista, 2 -A vista no cartão, 3 -2x no cartão, 4 -3x no cartão:'))
valBrut = 0.0
if condPag == 1:
    valBrut = preco - (preco * 0.10)
elif condPag == 2:
    valBrut = preco - (preco * 0.05)
elif condPag == 3:
    valBrut = preco
elif condPag == 4:
    valBrut = preco + (preco * 0.20)
print('O valor total a pagar é de R$ {:.2f}'.format(valBrut))
