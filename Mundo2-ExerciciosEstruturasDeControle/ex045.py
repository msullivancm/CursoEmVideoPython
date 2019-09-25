from time import sleep
from random import randrange
while 1 == 1:
    jog = int(input("Escolha 1 para Pedra, 2 para Papel, 3 para Tesoura: "))
    escolha = {1:"Pedra", 2:"Papel", 3:"Tesoura"}
    comp = randrange(1,3,1)
    print('Computador escolhendo...')
    sleep(3)
    if comp == 1 and jog == 2:
        print('Computador escolheu {} e você escolheu {}'.format(escolha[1], escolha[2]))
        print('Você ganhou!')
    elif comp == 1 and jog == 3:
        print('Computador escolheu {} e você escolheu {}'.format(escolha[1], escolha[3]))
        print('Computador ganhou!')
    elif comp == 1 and jog == 1:
        print('Computador escolheu {} e você escolheu {}'.format(escolha[1], escolha[1]))
        print('Empate!')
    elif comp == 2 and jog == 1:
        print('Computador escolheu {} e você escolheu {}'.format(escolha[2], escolha[1]))
        print('Computador ganhou!')
    elif comp == 2 and jog == 2:
        print('Computador escolheu {} e você escolheu {}'.format(escolha[2], escolha[2]))
        print('Empate!')
    elif comp == 2 and jog == 3:
        print('Computador escolheu {} e você escolheu {}'.format(escolha[2], escolha[3]))
        print('Você ganhou!')
    elif comp == 3 and jog == 1:
        print('Computador escolheu {} e você escolheu {}'.format(escolha[3], escolha[1]))
        print('Você ganhou!')
    elif comp == 3 and jog == 2:
        print('Computador escolheu {} e você escolheu {}'.format(escolha[3], escolha[2]))
        print('Computador ganhou!')
    elif comp == 3 and jog == 3:
        print('Computador escolheu {} e você escolheu {}'.format(escolha[3], escolha[3]))
        print('Empate!')
