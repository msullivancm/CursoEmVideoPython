total = maiscaro = customaisbarato = 0.00
maisbarato = ''
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))

    total += preco
    if preco > 1000.00:
        maiscaro += 1
    if preco < customaisbarato or customaisbarato == 0:
        customaisbarato = preco
        maisbarato = nome
    continua = ''
    while continua != 's' and continua != 'n':
        continua = input('Quer continuar? [s/n]').lower()
    if continua == 'n':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maiscaro:.0f} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisbarato} que custa R${customaisbarato:.2f}')
