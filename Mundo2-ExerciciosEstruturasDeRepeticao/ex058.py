from time import sleep
from random import randrange

palpite = 0
fim = 0
while fim != 1:
    numero = int(input('Digite um número de 0 a 10 e veja se acerta: '))
    palpite += 1
    print('Pensando...')
    sleep(3)
    comp = randrange(1, 10)
    if numero == comp:
        print('Você acertou.')
        print('Você usou {} palpites até acertar.'.format(palpite))
        fim = 1
    else:
        print('Você errou.')
