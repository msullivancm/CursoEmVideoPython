c = 1
while c != 0:
    sexo = str(input('Informe seu sexo: [M/F]:')).upper()
    if sexo != 'M' and sexo != 'F':
        c = 1
        print('Digite M ou F somente.')
    else:
        c = 0
print('fim')