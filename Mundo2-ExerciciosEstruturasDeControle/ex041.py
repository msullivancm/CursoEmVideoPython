from datetime import date

ano = int(input('Informe o ano de nascimento: '))
categoria = date.today().year - ano
if categoria <= 9:
    print('Mirim')
elif categoria <= 14:
    print('Infantil')
elif categoria <= 19:
    print('Junior')
elif categoria <= 20:
    print('Sênior')
else:
    print('Master')
