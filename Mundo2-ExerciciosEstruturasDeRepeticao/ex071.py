cedula = 50
contacedula = 0
valor = int(input('Qual será o valor a ser sacado R$'))
total = valor
while total != 0:
    contacedula = total // cedula
    total = total - (contacedula * cedula)
    print(f'São {contacedula} de R$ {cedula}')
    if total < 50:
        cedula = 20
    if total < 20:
        cedula = 10
    if total < 10:
        cedula = 1