nome = input('Qual é o seu nome? ')
if nome == 'Sullivan':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in ('Cláudia', 'Ana'):
    print('Nome de mulher.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))