peso = float(input('Informe seu peso: Kg'))
altura = float(input('Informe sua altura: m'))
imc = peso/(altura * altura)
if imc < 18.5:
    print('IMC= {:.2f}. Abaixo do peso'.format(imc))
elif imc >=18.5 and imc < 25:
    print('IMC= {:.2f}. Peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC= {:.2f}. Sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC= {:.2f}. Obsidade'.format(imc))
else:
    print('IMC= {:.2f}. Obesidade mórbida'.format(imc))
