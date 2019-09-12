alt = float(input('Informe a altura em metros: '))
lar = float(input('Informe a largura em metros: '))
area = alt * lar
print('A área da parede a ser pintada é de {:.2f}m2.\n E serão necessários {} litros de tinta.'.format(area, area/2))
