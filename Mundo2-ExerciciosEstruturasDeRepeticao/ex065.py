count = 0
total = 0
maior = 0
menor = 9999999999
while True:
    n = int(input('Digite um número: '))
    total = total + n
    count += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    go = str(input("Deseja continuar? [S/N]: ")).upper()
    if go == 'N':
        break
print('média={:.2f}. O maior={} e o menor={}'.format((total/count), maior, menor))
