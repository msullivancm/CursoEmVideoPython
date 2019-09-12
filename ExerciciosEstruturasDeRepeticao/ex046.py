from time import sleep
print('Início da contagem...')
for i in range(10, 0, -1):
    print('Contando: {}'.format(i))
    sleep(1)
print('BOOM!!!')