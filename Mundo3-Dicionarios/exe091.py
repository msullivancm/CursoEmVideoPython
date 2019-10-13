from random import randint
from time import sleep
jogadores = dict()
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1,6)
    sleep(1)
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('Ranking: ')
count = 0
for item in sorted(jogadores, key = jogadores.get):
    count+=1
    print(f'{count}o lugar: {item} com {jogadores[item]}')
    sleep(1)
