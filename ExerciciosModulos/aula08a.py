from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
raizarredondadaparacima= ceil(raiz)
raizarredondadaparabaixo= floor(raiz)
print('A raiz quadrada é {}'.format(raiz))
print('Arredondando pra cima {}'.format(raizarredondadaparacima))
print('Arredondando para baixo {}'.format(raizarredondadaparabaixo))