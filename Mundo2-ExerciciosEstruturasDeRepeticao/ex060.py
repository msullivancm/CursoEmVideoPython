n = int(input('Digite um número: '))
fat = 1
i = 2
fattxt = str(n)
ifattxt = n
while i <= n:
    fattxt = fattxt + 'X' + str(ifattxt-1)
    ifattxt -= 1
    fat = fat * i
    i = i + 1
print('O fatorial de {}!={}={}'.format(n, fattxt, fat))