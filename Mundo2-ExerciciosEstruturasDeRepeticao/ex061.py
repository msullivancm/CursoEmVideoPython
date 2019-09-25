termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
cont = 1
while cont <= 10:
    print('Termo: {}'.format(termo))
    termo += razao
    cont += 1
print('Esta é a progressão dos primeiros 10 termos.')