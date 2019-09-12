for i in range(0,6):
    print('Oi')
print('Fim')

for i in range(0,6,2):
    print(i)
print('Fim')

for i in range(6,0,-1):
    print(i)
print('Fim')

n = int(input('Digite um número: '))
for i in range(0, n+1):
    print(i)
print('Fim')

inicio = int(input('Digite um número de início: '))
fim = int(input('Digite um número de fim: '))
passo = int(input('Digite um número de passo: '))
for i in range(inicio, fim+1, passo):
    print(i)
print('Fim')

s = 0
for i in range(0,4):
    n = int(input('Digite um número: '))
    s += n
print('O somatório deu {}'.format(s))