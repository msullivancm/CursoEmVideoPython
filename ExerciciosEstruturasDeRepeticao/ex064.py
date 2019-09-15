cont = 1
n = 0
tot = 0
while n != 999:
    n = int(input('Informe um número ou 999 para encerrar: '))
    if n != 999:
        tot += n
        cont += 1
print('Foram digitados {} números e a soma deles é {}'.format(cont-1, tot))
