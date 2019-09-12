n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))
media = (n1+n2)/2
if media < 5.0:
    print('Reprovado.')
elif media >= 5.0 and media < 6.9:
    print('Em recuperação.')
elif media > 7.0:
    print("Aprovado.")