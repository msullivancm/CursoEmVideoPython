from datetime import date
maior = 0
menor = 0
for i in range(0, 7):
    data = int(input('Informe o ano de nascimento: '))
    if date.today().year - data >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas tem maior idade e {} não tem.'.format(maior, menor))
