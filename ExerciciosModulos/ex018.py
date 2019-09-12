import math
an = float(input('Informe o valor do ângulo: '))
se=math.sin(math.radians(an))
co=math.cos(math.radians(an))
ta=math.tan(math.radians(an))
print('O seno é {:.3f}, \ncoseno é {:.3f} \ne a tangente é {:.3f}'.format(se,co,ta))
