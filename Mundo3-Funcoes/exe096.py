def titulo(tit):
    print(f'{tit:^30}')
    print('-' * 30)

def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m2.')

titulo('Controle de terrenos')
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg,comp)
