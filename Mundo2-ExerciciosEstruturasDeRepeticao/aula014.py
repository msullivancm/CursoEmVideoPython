'''for c in range(1,10):
    print(c)
print('Fim')
'''
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = (input('Quer continuar [S,N]: ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n!= 0:
        if n % 2 == 0:
            par+=1
        else:
            impar+=1
print('Você digitou {} pares e {} impares'.format(par, impar))