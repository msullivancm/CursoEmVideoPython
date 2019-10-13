from random import randint
from time import sleep

numeros = list()
pares = list()

def sorteia():
    for i in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Sorteando {len(numeros)} da lista: ', end='')
    for i in numeros:
        print(f'{i}', end=' ')
        sleep(1)
    print('PRONTO!')


def somaPar(lst):
    for i in lst:
        if i % 2 == 0:
            pares.append(i)
    print(f'Somando os valores pares de {numeros}, temos {sum(pares)}')

sorteia()
somaPar(numeros)