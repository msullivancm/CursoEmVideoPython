from random import randrange
from time import sleep
print('O computador vai pensar num número de 0 a 5, tente adivinhar.')
num = int(input('Tente advinhar o número de 0 a 5 que o computador escolheu: '))
comp = randrange(0,5,1)
print('Processando...')
sleep(3)
if num == comp:
    print('Você venceu!')
else:
    print('O computador escolheu o número {}. Você perdeu.'.format(comp))
