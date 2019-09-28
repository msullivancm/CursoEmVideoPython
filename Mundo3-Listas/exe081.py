lista = []
count = 0
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = ''
    while continuar not in ('s','n'):
        continuar = input('Quer continuar? [S/N]').lower()
    count +=1
    if continuar == 'n':
        break
print(f'Você digitou {count} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if lista.__contains__(5):
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'Lista não possui o valor 5.')
