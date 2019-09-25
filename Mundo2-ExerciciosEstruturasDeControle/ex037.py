num = int(input('Informe um número: '))
escolha = int(input('Selecione 1 para conversão em binário, 2 para conversão em octal e 3 para conversão em hexadecimal: '))
if escolha == 1:
    print('Convertido para binário: {}'.format(bin(num)[2:]))
elif escolha == 2:
    print('Convertido para octal: {}'.format(oct(num)[2:]))
elif escolha == 3:
    print('Convertido para hexa: {}'.format(hex(num)[2:]))
