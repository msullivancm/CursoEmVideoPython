from time import sleep
def conta(ini, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    if ini > fim:
        passo *= -1
    for i in range(ini, fim, passo):
        print(f'{i}', end=' ', flush=True)
        sleep(1)
    print(f'{fim} FIM!')


def linha():
    print('=-' * 40)


linha()
conta(1, 10, 1)
linha()
conta(10, 0, 2)
linha()
print(f'Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
conta(i, f, p)