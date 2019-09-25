maior = 0
menor = 1000000
for i in range(0, 5):
    num = int(input('Informe o peso: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print('O maior peso é {} e o menor é {}'.format(maior, menor))
