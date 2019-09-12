a = float(input('Informe comprimento da reta 1: '))
b = float(input('Informe comprimento da reta 2: '))
c = float(input('Informe comprimento da reta 3: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Estas retas podem formar um triângulo.')
    if a == b and b == c:
        print('O triângulo é Equilátero.')
    elif a==b or b==c or c==a:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')

else:
    print('Estas retas não podem formar um triângulo.')
