termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
cont = 10
while cont > 0:
    print('Termo: {}'.format(termo))
    termo += razao
    cont -= 1
    if cont == 0:
        t = int(input('Deseja ver mais quantos termos: '))
        if t != 0:
            cont = t
        else:
            cont = 0
