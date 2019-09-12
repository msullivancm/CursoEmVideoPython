cidade = input('Digite o nome da sua cidade: ')
comeco = cidade.split()
if comeco[0].lower() == 'santo':
    print('Sua cidade começa com a palavra SANTO')
#or
print('='*20)
print(cidade.strip().lower()[:5] =='santo')
