from time import sleep
def maior(* val):
    tam = len(val)
    print('Analisando os valores passados...')
    valores = ''
    for i in val:
        print(f'{i}', end=' ')
        sleep(1)
    print(f'foram informados {tam} valores ao todo.')
    maior = 0
    for i in val:
        if maior < i:
            maior = i
    print(f'O maior valor informado foi {maior}')


def linha():
    print('=-' * 40)


linha()
maior(2,9,4,5,7,1)
linha()
maior(4,7,0)
linha()
maior(1,2)
linha()
maior(6)
linha()
maior()