n1 = int(input('Digite um número inteiro para ver sua tabuada: '))
print('='*12)
for i in range(1, 11):
    print('{} x {:2} = {}'.format(n1, i, n1*i))
print('='*12)
print('Tabuada de <<{:=^5}>> completa'.format(n1))