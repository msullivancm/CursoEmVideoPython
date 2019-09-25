numero = input('Informe um número entre 0 e 9999: ')
if len(numero)>=1:
    print('Unidade: {}'.format(numero[len(numero)-1]))
if len(numero)>=2:
    print('Dezena: {}'.format(numero[len(numero)-2]))
if len(numero)>=3:
    print('Centena: {}'.format(numero[len(numero)-3]))
if len(numero)>=4:
    print('Milhar: {}'.format(numero[len(numero)-4]))
#ou
print('='*20)
numeroint = int(numero)
u = numeroint // 1 % 10
d = numeroint // 10 % 10
c = numeroint // 100 % 10
m = numeroint // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))