lista = []
expressao = input('Digite a expressão: ')
for f in expressao:
    lista.append(f)
if lista.count('(') == lista.count(')'):
    print('Expressão correta!')
else:
    print('Sua expressão está errada!')

