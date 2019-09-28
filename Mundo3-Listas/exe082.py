lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ''
    while continuar not in ('s','n'):
        continuar = input('Quer continuar? [S,N]').lower()
    if continuar == 'n':
        break

print(f'A lista completa é {lista}')

par = []
imp = []
for l in lista:
    if l % 2 == 0:
        par.append(l)
    else:
        imp.append(l)

print(f'A lista de pares é {par}')
print(f'A lista de impares é {imp}')
