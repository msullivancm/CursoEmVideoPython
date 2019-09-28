lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if lista.__contains__(valor):
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
    continuar = ''
    while continuar not in ('s','n'):
        continuar = input('Quer continuar? [S/N]').lower()
    if continuar == 'n':
        break

lista.sort()
print(f'Você digitou os valores {lista}')

