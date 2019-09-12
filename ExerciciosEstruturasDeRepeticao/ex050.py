s = 0
for i in range(1, 7):
    n = int(input('Informe um número inteiro: '))
    if n % 2 == 0:
        s += n
print('Soma é {}'.format(s))