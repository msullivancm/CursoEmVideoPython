from math import hypot
catOposto = float(input('Informe o comprimento do cateto oposto do triângulo retângulo: '))
catAdjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = hypot(catOposto, catAdjacente)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))