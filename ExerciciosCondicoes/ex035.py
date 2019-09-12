a = float(input('Informe comprimento da reta 1: '))
b = float(input('Informe comprimento da reta 2: '))
c = float(input('Informe comprimento da reta 3: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Estas retas podem formar um triângulo.')
else:
    print('Estas retas não podem formar um triângulo.')
