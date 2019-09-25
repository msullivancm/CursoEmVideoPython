from datetime import date

ano = int(input('Informe o ano de nascimento: '))
idade = date.today().year - ano
if idade == 18:
    print('É hora de se alistar.')
elif idade > 18:
    print('Já passou {} anos do alistamento.'.format((idade-18)))
else:
    print('Ainda faltam {} anos para se alistar.'.format(18-idade))