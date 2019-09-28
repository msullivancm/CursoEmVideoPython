from random import randint
from time import sleep
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
numeros = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
cont = 0
while cont < quant:
    for n in range(0, 6):
        n = randint(0, 60)
        if numeros.count(n) == 0:
            numeros.append(n)
        else:
            numeros.append(randint(0, 60))
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    cont += 1
print(f'-=-=-= SORTEANDO {quant} JOGOS -=-=-=')
for i in range(0, quant):
    print(f'Jogo {i}: {jogos[i]}')
    sleep(1)
print(f'{"BOA SORTE!":=^30}')
