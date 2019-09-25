termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

for i in range(1, 11):
    print('Termo: {}'.format(termo))
    termo += razao
print('Esta é a progressão dos primeiros 10 termos.')
