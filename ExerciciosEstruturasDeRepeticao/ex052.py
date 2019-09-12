num = int(input('Informe um número: '))
primo = True
for i in range(1, num):
    if i != 1 and i != num:
        if num % i == 0:
            primo = False
if primo:
    print('O número {} é primo.'.format(num))
else:
    print('O número {} não é primo.'.format(num))

